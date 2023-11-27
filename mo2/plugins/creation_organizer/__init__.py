import mobase
from .creation_organizer_plugin import CreationOrganizerPlugin


def createPlugin() -> mobase.IPlugin:
    return CreationOrganizerPlugin()
