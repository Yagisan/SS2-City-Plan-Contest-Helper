from typing import List

import mobase
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import PyQt5.QtWidgets as qtw

from .logic.co_constants import PLUGIN_NAME, AUTHOR, DESCRIPTION, FAILS
from .interface.co_dialog import CreationOrganizerDialog


class CreationOrganizerPlugin(mobase.IPluginTool):
    def __init__(self):
        super().__init__()
        self.error_list = []

    def init(self, organizer: mobase.IOrganizer):
        self._organizer = organizer
        return True

    def name(self) -> str:
        return PLUGIN_NAME

    def author(self) -> str:
        return AUTHOR

    def description(self) -> str:
        return self.__tr(DESCRIPTION)

    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo(0, 0, 6, mobase.ReleaseType.FINAL)

    def isActive(self) -> bool:
        # I added bool
        return bool(self._organizer.pluginSetting(self.name(), "enabled"))

    def settings(self) -> List[mobase.PluginSetting]:
        return [mobase.PluginSetting("enabled", "enable this plugin", True)]

    def localizedName(self) -> str:
        # Use self.__tr to wrap string you want translatable.
        return self.__tr(PLUGIN_NAME)

    def __tr(self, txt: str) -> str:
        # The first argument must EXACTLY match the class name:
        return QApplication.translate("CreationOrganizerPlugin", txt)

    def displayName(self) -> str:
        return PLUGIN_NAME

    def display(self):  # noqa: E501
        self._organizer.pluginList().onRefreshed(self.post_refresh)
        self.dialog = CreationOrganizerDialog(
            self.__parentWidget, self._organizer, self.error_list
        )
        self.dialog.finished.connect(self.display_finished)
        self.dialog.btn_pressed()  # open() #to display button

    def display_finished(self, val):
        self.dialog.close()
        if val:
            box = qtw.QMessageBox(self.__parentWidget)
            box.critical(
                self.__parentWidget, self.__tr(FAILS[val]), self.__tr(FAILS[val + 1])
            )
            box.deleteLater()
        if self.error_list:
            errors = self.__tr(str().join(self.error_list)[:-1])
            print(errors)
            count = 2 if len(self.error_list) > 1 else 1
            box = qtw.QMessageBox(self.__parentWidget)
            box.critical(
                self.__parentWidget,
                FAILS[4 + count],
                f"{FAILS[5 + count]}{errors}",
            )
            box.deleteLater()
        self.dialog.deleteLater()
        self.dialog = None

    def post_refresh(self):
        if self.dialog != None and self.dialog.finish_process:
            self.dialog.post_refresh()

    def icon(self) -> QIcon:
        return QApplication.style().standardIcon(qtw.QStyle.SP_DesktopIcon)

    def tooltip(self) -> str:
        return self.__tr(f"{PLUGIN_NAME}: {DESCRIPTION}")

    def setParentWidget(self, widget):
        self.__parentWidget = widget
