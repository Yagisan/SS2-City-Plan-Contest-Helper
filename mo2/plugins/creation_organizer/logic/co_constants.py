PLUGIN_NAME = "Creation Organizer"
AUTHOR = "weds4"
DESCRIPTION = "Move Creation Club content and enable dependent mods"
SKYRIM_SE = "Skyrim Special Edition"
JSON_PATH = ".\\plugins\\creation_organizer\\creation_organizer.json"
SUFFIXES = (".esm", ".esl", ".bsa")
REG_PATH = "SOFTWARE\WOW6432Node\Bethesda Softworks\Skyrim Special Edition"
FAILS = [
    "No Fails",
    "Wrong Game!",
    "You tried to run this on a game that isn't Skyrim SE",
    "JSON not Found",
    f"ModOrganizerInstallFolder{JSON_PATH[1:]} was not found. Please create and configure the JSON file.",
    "Reported Errors",
    "Creation Organizer completed with an error. See below:\n",
    "Reported Errors",
    "Creation Organizer completed with errors. See below:\n",
]
