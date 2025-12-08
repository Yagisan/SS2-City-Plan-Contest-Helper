# Yagisan's Sim Settlements 2 City Plan Contest Helper

![GitHub all releases](https://img.shields.io/github/downloads/Yagisan/SS2-City-Plan-Contest-Helper/total?logo=GitHub&style=for-the-badge)![GitHub issues](https://img.shields.io/github/issues/Yagisan/SS2-City-Plan-Contest-Helper?logo=GitHub&style=for-the-badge)![Discord](https://img.shields.io/discord/958710541017317397?label=Yagisan%27s%20Discord&logo=discord&style=for-the-badge)

Yagisan's Sim Settlements 2 City Plan Contest Helper was a curated modlist specifically designed for entrants in the Sim Settlements 2 City Plan contest.

**After 4 seasons, and many, many years of entries, the City Plan contest has come to an end. The new purpose of this list is to carry on the spirit of the competition rules, and to provide a list where city plan builders can produce stunning city plans.**

It contains F4SE, Buffout 4 and several other F4SE based bugfixes and useful building utilities. In addition it contains the UFO4P, SimSettlements 2, all of its dependencies, and finally it contains all SimSettlements 2 addon packs that are known to be actively maintained and with cooperative authors.

This list **requires** Creation Club content, and enable SimSettlements 2 plots that use Creation Club content.

**This list will coexist with your existing installation.**

![CPC_Heroshot](assets/images/SS2_CPC_Hero_20240516.webp)

 | [![patreon](https://raw.githubusercontent.com/Yagisan/The-Bustling-Valley/main/assets/images/become_a_patron_button.png)](https://patreon.com/yagisan) | [![ko-fi](https://raw.githubusercontent.com/Yagisan/The-Bustling-Valley/main/assets/images/support_on_kofi_button.png)](https://ko-fi.com/yagisan) | [![Discord Banner 2](https://discordapp.com/api/guilds/958710541017317397/widget.png?style=banner2)](https://discord.gg/rB5RFgHhUD) |
| - | - | - |

- [Yagisan's Sim Settlements 2 City Plan Contest Helper](#yagisans-sim-settlements-2-city-plan-contest-helper)
- [Preamble](#preamble)
- [Quick Links](#quick-links)
- [Installation](#installation)
  - [Pre-Installation](#pre-installation)
    - [Installing Microsoft Visual C++ Redistributable Package](#installing-microsoft-visual-c-redistributable-package)
    - [Steam Config](#steam-config)
      - [Disable the Steam Overlay](#disable-the-steam-overlay)
      - [Change Steams Update Behaviour](#change-steams-update-behaviour)
      - [Set the Game language to English](#set-the-game-language-to-english)
    - [Reverting a "cleaned" Fallout 4](#reverting-a-cleaned-fallout-4)
      - [Start Fallout 4](#start-fallout-4)
      - [Creation Club](#creation-club)
    - [Using Wabbajack](#using-wabbajack)
      - [Preparations](#preparations)
      - [Downloading and Installing](#downloading-and-installing)
        - [Automatic - Recommended](#automatic---recommended)
        - [Manual - Not Recommended](#manual---not-recommended)
      - [Problems with Wabbajack](#problems-with-wabbajack)
  - [Post-Installation](#post-installation)
- [Setting Graphics options](#setting-graphics-options)
- [Starting the Game](#starting-the-game)
- [Updating](#updating)
- [Starting the game](#starting-the-game-1)
- [Other Post Installation FAQ](#other-post-installation-faq)
  - [Adjusting the resolution](#adjusting-the-resolution)
  - [Removing the Modlist](#removing-the-modlist)
  - [Contact and Technical Support](#contact-and-technical-support)

# Preamble

**The new purpose of this list is to carry on the spirit of the competition rules, and to provide a list where city plan builders can produce stunning city plans.**

# Quick Links

- [Patreon](https://patreon.com/yagisan) contains update posts and provides a way of showing support for the project.
- [Ko-fi](https://ko-fi.com/yagisan) contains update posts and provides a way of showing support for the project.
- [Downloads](https://github.com/Yagisan/SS2-City-Plan-Contest-Helper/releases) for the most recent releases.
- [Wabbajack](https://github.com/wabbajack-tools/wabbajack/releases) for the tool to install this modlist.
- [Issues](https://github.com/Yagisan/SS2-City-Plan-Contest-Helper/issues) for technical support with this mod list.
- [Discord](https://discord.gg/rB5RFgHhUD) for community support with the mod list.

# Installation

## Pre-Installation

These steps are only needed if you install this Modlist for the first time. If you update the Modlist, jump straight to [Updating](#updating).

### Installing Microsoft Visual C++ Redistributable Package

It is unlikely that you are missing this. However it is needed for MO2 and several plugins, so please download it and install it anyway from [Microsoft](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads). Download the x64 version under "Visual Studio 2015, 2017 and 2019". This is [Direct link](https://aka.ms/vs/16/release/vc_redist.x64.exe) if you can't find it.

### Steam Config

#### Disable the Steam Overlay

![Steam_General_Settings](assets/images/Steam_General_Settings.webp)

The Steam Overlay can cause issues with ENB and is recommended to be turned off.
**Please note that this mod list does not use an ENB.**

Open the Properties window (right click the game in your Library->Properties), navigate to the _General_ tab and un-tick the _Enable the Steam Overlay while in-game_ checkbox. You should also un-tick the _Keep games saves in the Steam Cloud_.

#### Change Steams Update Behaviour

![Steam_Update_Settings](assets/images/Steam_Update_Settings.webp)

Fallout 4 is still being updated by Bethesda (they only add Verified Creations content). Whenever the game updates, the entire modding community goes silent for the next one or two weeks because some mods need to be updated to the latest game runtime version.

To ensure that Steam does not automatically update the game for you, head over to the Properties window, navigate to the _Updates_ tab and change _Automatic updates_ to _Only update this game when I launch it_.

#### Set the Game language to English

![Steam_Language_Settings](assets/images/Steam_Language_Settings.webp)

This modlist is in English, and most of the mods you find are in English. **I can not give support to people with a non-English game**.

Open the Steam Properties window, navigate to the _Language_ tab and select _English_ from the dropdown menu.

### Reverting a "cleaned" Fallout 4

A lot of older modding guides recommended "cleaning" the Fallout 4 master esm files. **If you have "cleaned" your files this list will fail to install.** If you have done this, please re-verify the Fallout 4 files through Steam. Steam will fix your Fallout 4 master files, and you can then reinstall this list.

#### Start Fallout 4

![Fallout_Launcher](assets/images/Fallout_Launcher.webp)

On a brand new installation of Fallout 4, or after reverting a "cleaned" Fallout 4, you will need to launch Fallout 4 before you can install this mod list. Start the Launcher and open the _Options_ menu.

![Fallout_Launcher_Options](assets/images/Fallout_Launcher_Options.png)

1. Click on _Ultra_
2. Set the  _Resolution_ to your monitor's native values
3. Set _Antialiasing_ to _TAA_
4. **Do not** check _Windowed Mode_ and _Borderless_

**Start the game and exit once you're in the main menu.**

#### Creation Club

![Creation_Club_Purchased](assets/images/Creation_Club_Purchased_AE.png)

If you own any items from the Creation Club, they are not automatically reinstalled when you install Fallout 4. To reinstall Creation Club items, you must launch the game, select the **Creations** menu option, press "O" and select the Download all owned Creation Club Creations option.

**Creation Club items are REQUIRED in this mod list.**

The following Creation Club Content is currently required.

* Arcade Workshop Pack
* Charlestown Condo
* Coffee and Donuts Workshop Pack
* Home Decor Workshop Pack
* Modern Furniture Workshop Pack
* Nuka-Cola Collector Workshop
* Noir Penthouse
* Holiday Workshop Pack
* Shroud Manor
* Neon Flats
* Capital Wasteland Mercenaries
* Captain Cosmos
* Settlement Ambush Kit

**Players must obviously own that Creation Club content, and must have downloaded it via the in-game launcher, in their main Fallout 4 installation.**

### Using Wabbajack

#### Preparations

Grab the latest release of Wabbajack from [the Nexus](https://www.nexusmods.com/site/mods/403) and place the `Wabbajack.exe` file in a _working folder_.  The recommended working folder is `C:\WJ\WabbaJack`. This folder **must not** be in a _common folders_ like your Desktop, Downloads or Program Files folder.

#### Downloading and Installing

The download and installation process can take a very long time depending on your system specs. Wabbajack will calculate the amount of threads it will use at the start of the installation. To have the highest amount of threads and thus the fastest speed, it is advised to have the working folder on an SSD.

##### Automatic - Recommended

1. Open Wabbajack.
2. Click on **Browse Modlists**. In the Games drop down tab, select Fallout 4. Enable "Non-featured". Select Sim Settlements 2 City Plan Contest Helper from the selection.
3. Set the _installation location_. The recommended installation location is `C:\WJ\CPC`.  This folder **must not** be in a _common folders_ like your Desktop, Downloads or Program Files folder. **The rest of this document will assume you are using the recommended installation path.** Do not install to a _OneDrive_ folder.
4. Set the _download location_. The recommended download location is `C:\WJ\CPC_downloads`.  This folder **must not** be in a _common folders_ like your Desktop, Downloads or Program Files folder. Do not install to a _OneDrive_ folder.
5. **If you have installed a previous version please ensure Installation Location and Download Location match your previous Installation and Download Directories.**
6. Then press the Install button. The Sim Settlements 2 City Plan Contest Helper will now install/update automatically.
7. Wait for Wabbajack to finish
8. If you run into any issues see the next section. If the installation is successful, proceed to [Post-Installation](#post-installation).

##### Manual - Not Recommended

1. [Download the latest released .wabbajack file from GitHub](https://github.com/Yagisan/SS2-City-Plan-Contest-Helper/releases). Save it to a temporary folder. The recommended temporary folder is `C:\Temp\CPC`.
2. Open Wabbajack.
3. Click on Install form Disk. Set the target modlist to `C:\Temp\CPC\Yagisan's SimSettlements 2 City Plan Contest Helper.wabbajack`
4. Set the _installation location_. The recommended installation location is `C:\WJ\CPC`.  This folder **must not** be in a _common folders_ like your Desktop, Downloads or Program Files folder. **The rest of this document will assume you are using the recommended installation path.**
5. Set the _download location_. The recommended download location is `C:\WJ\CPC_downloads`.  This folder **must not** be in a _common folders_ like your Desktop, Downloads or Program Files folder.
6. If you have existing downloads from Vortex or MO2, you may copy the `.zip`, `.7z`, or `.rar` files only to the _download location_. The recommended download location is `C:\WJ\CPC_downloads`. If the file you copy is exactly the same as what this wabbajack users, it will not be downloaded again, saving bandith.
7. Click the Install button. Wabbajack will check your downloads for matching files, and download any files it needs.
8. Wait for Wabbajack to finish
9. If you run into any issues see the next section. If the installation is successful, proceed to [Post-Installation](#post-installation).

#### Problems with Wabbajack

There are a lot of different scenarios where Wabbajack will produce an error. I recommend re-running Wabbajack before posting anything. Wabbajack will continue where it left off so you will not lose progress.

**Could not download x**:

If a mod updated and the old files were deleted, it is impossible to download them. You will need to be patient and wait for me to update the modlist.

**Wabbajack could not find my game folder**:

Wabbajack will not work with a pirated version of the game. If you own the game on Steam, go back to the [Pre-Installation](#pre-installation) step.

## Post-Installation

# Setting Graphics options

Head over to the installation folder and locate an executable named `ModOrganizer.exe` and launch it. This will be `C:\WJ\CPC\ModOrganizer.exe` if you have followed the recommended settings. Once it is launched, there will be a dropdown box on the top right and a big run button right next to it.

 Ensure it is set to **Fallout Launcher** by selecting it in the dropdown box and then hitting the run button. You have to run the Fallout Launcher through Mod Organizer 2 in order update your graphics settings for Yagisan's SimSettlements 2 City Plan Contest Helper.

 ![Fallout_Launcher_Options](assets/images/Fallout_Launcher_Options.png)

1. Click on _Ultra_
2. Set the  _Resolution_ to your monitor's native values
3. Set _Antialiasing_ to _TAA_
4. **Do not** check _Windowed Mode_ and _Borderless_
5. Click OK.
6. **Quit the Fallout 4 Launcher**

# Starting the Game

Head over to the installation folder and locate an executable named `ModOrganizer.exe` and launch it. This will be `C:\WJ\CPC\ModOrganizer.exe` if you have followed the recommended settings. Once it is launched, there will be a dropdown box on the top right and a big run button right next to it.

Ensure it is set to **F4SE** by selecting it in the dropdown box and then hitting the run button. You have to run F4SE through Mod Organizer 2 in order to play Yagisan's SimSettlements 2 City Plan Contest Helper.

# Updating

If this Modlist receives an update please check the [Changelog](CHANGELOG.md) before doing anything. The [Changelog](CHANGELOG.md) will advise you of any changes to addons. **Back up your save games before updating** Save files should be untouched when updating.

**Wabbajack will delete all files that are not part of the Modlist when updating!**

Your downloads folder will not be touched.

Updating is like installing. You only have to make sure that you select the same path and tick the _overwrite existing Modlist_ button.

# Starting the game

After starting the game, there are a few clean saves included. Load one, wait a few moments for mods to initialise, then exit Vault 111.

It is **very** important that you wait until all the messages in the top left corner have finished. Now would be an excellent time to go make a cup of tea or coffee. Once these messages have finished, press `ESCAPE` and create a manual save before you continue, and proceed to exit the vault.

At this point a second group of mods will begin initialising, including the city plan contest holotape. Answer the questions prompted by the holotape, press the `~` key, then type `tgm`, then press the `ENTER` key to turn on god mode. The remainder of the mods will now initialise.

It is **very** important that you wait until all the messages in the top left corner have finished. Now would be an excellent time to go make a another cup of tea or coffee. Once these messages have finished, open the MCM, and in `MCM Settings manager` apply the supplied `Yagisan's City Plan Contest` preset. Now you are ready to go the the contest location, and start building.

# Other Post Installation FAQ

## Adjusting the resolution

By default the list ships with a safe 720p fullscreen configuration. To change this, click on `F4SE` in the dropdown list. Select `Fallout 4 Launcher` then click run. Adjust your settings as in vanilla, then  quit the launcher. Click on `Fallout 4 Launcher` in the dropdown list. Select `F4SE` then click run to start the game.

## Removing the Modlist

Simply delete the installation folder (`C:\WJ\CPC` if you have been following this guide) and that will remove it, but why would you want to?

## Contact and Technical Support

Please check the [Issues](https://github.com/Yagisan/SS2-City-Plan-Contest-Helper/issues) (open **and** closed ones) on GitHub first if you have any problems. The same goes for _Enhancements_ or _Feature/Mod Requests_. If you believe you have found a bug in the mod list, please file bug report [here](https://github.com/Yagisan/SS2-City-Plan-Contest-Helper/issues) with as much information as possible to replicate the issue. There is a [Support Discord](https://discord.gg/rB5RFgHhUD) for issues with the mod list. Requests for support on any other platform will be ignored. **DO NOT DM ME ON DISCORD. I WILL NOT PROVIDE SUPPORT FOR YOU IN DMS AND I WILL BLOCK YOU**.
