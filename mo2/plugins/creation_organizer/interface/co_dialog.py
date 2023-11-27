from json import load
import winreg
from pathlib import Path
from time import sleep

import PyQt5
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

import mobase
from ..logic.co_constants import JSON_PATH, SUFFIXES, SKYRIM_SE, REG_PATH


class CreationOrganizerDialog(qtw.QDialog):
    def __init__(
        self, parent: qtw.QMainWindow, organizer: mobase.IOrganizer, errors: list
    ) -> None:
        self.organizer = organizer
        super().__init__(parent)
        self.btn = qtw.QPushButton(self.__tr("Move and Enable CC and Mods"), self)
        self.btn.clicked.connect(self.btn_pressed)
        self.setLayout(qtw.QHBoxLayout())
        self.layout().addWidget(self.btn)
        self.errors = errors
        self.finish_process = False

    def __tr(self, txt: str) -> str:
        # The first argument must EXACTLY match the class name:
        return qtw.QApplication.translate("CreationOrganizerDialog", txt)

    def btn_pressed(self) -> None:
        """Call when btn is clicked"""
        self.co_procedure()

    def open(self):
        """to use later if I need it"""
        super().open()

    def co_procedure(self) -> int:
        """moves cc and enables dependant mods"""
        if not self.game_check():
            self.finished.emit(1)
            return 1
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        try:
            with winreg.OpenKey(reg, REG_PATH) as sky_key:
                registry_path = winreg.QueryValueEx(sky_key, "Installed Path")[0]
        except FileNotFoundError:
            registry_path = " "
        data_paths = (
            Path(f"{registry_path}data"),
            Path(f"{self.organizer.managedGame().gameDirectory().path()}\\data"),
            Path(self.organizer.overwritePath()),
        )
        move_or_copy = bool(data_paths[0] == data_paths[1])  # move if true else copy
        self.existing_ccs = {"move_or_copy": move_or_copy}
        if not Path(JSON_PATH).exists():
            self.finished.emit(3)
            return 3
        with open(JSON_PATH) as text:
            configuration = load(text)
        for key in configuration:
            if key[-4:] in (SUFFIXES):
                self.errors.append(f"{key} is not a valid JSON key.\n")
                continue
            paths = set()
            gen_paths = (
                Path(f"{data_path}\\{key}").with_suffix(i)
                for i in SUFFIXES
                for data_path in data_paths
            )
            for x in gen_paths:
                if x.exists():
                    paths.add(x)
            if paths:
                configuration[key]["files"] = list(paths)
                self.existing_ccs[key] = configuration[key]
        for key in self.existing_ccs:
            entry = self.existing_ccs[key]
            if isinstance(entry, bool):
                continue
            if not entry["move_to"] in self.mods.allMods():
                self.organizer.createMod(mobase.GuessedString(entry["move_to"]))
        self.organizer.refresh()
        self.finish_process = True
        return 0

    def post_refresh(self):
        self.finish_process = False
        for key in self.existing_ccs:
            entry = self.existing_ccs[key]
            if isinstance(entry, bool):
                continue
            file_paths = entry["files"]
            mod_path = self.mods.getMod(entry["move_to"]).absolutePath()
            for x in file_paths:
                try:
                    if self.existing_ccs["move_or_copy"]:
                        x.rename(f"{mod_path}\\{x.name}")
                    else:
                        Path(f"{mod_path}\\{x.name}").write_bytes(x.read_bytes())
                except PermissionError:
                    self.errors.append(
                        f'{x.name} could not be {"moved" if self.existing_ccs["move_or_copy"] else "copy"} due to a Permissions Error.\nIs the file already open?'
                    )
            if entry["enable_cc"]:
                self.mods.setActive(entry["move_to"], True)
            self.mods.setActive(entry["others_to_enable"], True)
        self.existing_ccs = []
        self.organizer.refresh()
        self.finished.emit(0)

    def game_check(self) -> bool:
        """check if game is Skyrim SE"""
        return bool(self.organizer.managedGame().gameName() == SKYRIM_SE)

    @property
    def mods(self) -> mobase.IModList:
        return self.organizer.modList()
