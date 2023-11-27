PLUGIN_NAME = "Creation Organizer"
AUTHOR = "weds4, yagisan"
DESCRIPTION = "Move Creation Club content and enable dependent mods"
SKYRIM_SE = "Fallout 4"
JSON_PATH = ".\\plugins\\creation_organizer\\creation_organizer.json"
SUFFIXES = (".esm", ".esl", ".ba2")
REG_PATH = "SOFTWARE\WOW6432Node\Bethesda Softworks\Fallout4"
FAILS = [
    "No Fails",
    "Wrong Game!",
    "You tried to run this on a game that isn't Fallout 4 (Steam Release)",
    "JSON not Found",
    f"ModOrganizerInstallFolder{JSON_PATH[1:]} was not found. Please create and configure the JSON file.",
    "Reported Errors",
    "Creation Organizer completed with an error. See below:\n",
    "Reported Errors",
    "Creation Organizer completed with errors. See below:\n",
]
