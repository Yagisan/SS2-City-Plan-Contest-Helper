# Changelog

- [Changelog](#changelog)
  - [Semantic Versioning](#semantic-versioning)
  - [3.26.2](#3262)
  - [3.26.1](#3261)
  - [3.26.0](#3260)
  - [3.25.1](#3251)
  - [3.25.0](#3250)
  - [3.24.2](#3242)
  - [3.24.1](#3241)
  - [3.24.0](#3240)
  - [3.23.1](#3231)
  - [3.23.0](#3230)
  - [3.22.2](#3222)
  - [3.22.1](#3221)
  - [3.22.0](#3220)
  - [3.21.1](#3211)
  - [3.21.0](#3210)
  - [3.20.4](#3204)
  - [3.20.3](#3203)
  - [3.20.2](#3202)
  - [3.20.1](#3201)
  - [3.20.0](#3200)
  - [3.19.3](#3193)
  - [3.19.2](#3192)
  - [3.19.1](#3191)
  - [3.19.0](#3190)
  - [3.18.1](#3181)
  - [3.18.0](#3180)
  - [3.17.0](#3170)
  - [3.16.2](#3162)
  - [3.16.1](#3161)
  - [3.16.0](#3160)
  - [3.15.2](#3152)
  - [3.15.1](#3151)
  - [3.15.0](#3150)
  - [3.14.4](#3144)
  - [3.14.3](#3143)
  - [3.14.2](#3142)
  - [3.14.1](#3141)
  - [3.14.0](#3140)
  - [3.13.2](#3132)
  - [3.13.1](#3131)

## Semantic Versioning

This modlist uses a modified semantic versioning to identify which competition it is targeted at, where given a version number SEASON.CONTEST.PATCH, increment the:

1. SEASON version when the contest season changes. **Contest rules will change.**
2. CONTEST version when the contest changes. **Contest rules may change between contests.**
3. PATCH version when hotfixes and/or updates are released mid-contest.

## 3.26.2

**Released:** `29 Oct 2023`

### Info <!-- omit in toc -->

Final release for the Unofficial Outpost Plan Contest at Pra's Boston Library Settlement, and Season 3 in general. All mods updated to the latest release available as of 6:30pm 29 Oct 2023 JST.

## 3.26.1

**Released:** `2 Oct 2023`

### Info <!-- omit in toc -->

This release is for the Unofficial Outpost Plan Contest at Pra's Boston Library Settlement. It fixes missed valid settlement objects, inability to rotate objects, and includes the latest release of SS2 as it has tools useful for fixing multiple settlement related data issues.

Please run "Clear all highlighting" in the Contest Holotape, wait for it to finish, then re-run "Check my settlement" in the Contest Holotape to fix highlighting. You may also want to run, in the SS2 Holotape, under Tools -> Advanced, "Recalculate NPC Counts", "Recalculate Resource Networks" and "Reset Network Distances Cache" to ensure that the SS2 internal data is correctly updated.

- The MCM Contest settings have been updated to fix slow rotation speed. Please open the MCM and reapply the City Plan Contest settings if you have already started building.
- City Plan Contest Helper has been edited by Yagisan to check for required outpost items. Updated to include Library items missed originally.
- Must use the supplied LibraryComp_Female or LibraryComp_Male save games to build with. These have been updated to turn off the Workshop Plus "Freeze time when building" option for new builders.

## 3.26.0

**Released:** `28 Sep 2023`

### Info <!-- omit in toc -->

This release is for the Unofficial Outpost Plan Contest at Pra's Boston Library Settlement.

- City Plan Contest Helper has been edited by Yagisan to check for required outpost items.
- Must use the supplied LibraryComp_Female or LibraryComp_Male save games to build with.

## 3.25.1

**Released:** `26 Sep 2023`

### Info <!-- omit in toc -->

- The SS2CPC Helper now supports both Steam and GoG releases of Fallout 4. (Once Wabbajack releases with Fallout 4 GoG support)
- Installation size has been reduced from 50GB to 15GB. 35GB saved!
- Updated to the most recent release of SimSettlements, and supported addons.
- It is intentionally not possible to edit the load order to add additional mods.
- Supported Creation Club content is now automatically enabled. (Technical limitations)
- Creation Organizer now only enables addons that depend on CC content.
- Creation Organizer does not work with GoG installations. (They don't have Creation Club).
- Startup and shutdown are slower, as it's now backing up and restoring files in your main Fallout 4 installation.
- Applying Yagisan's City Plan Contest MCM Settings will enable an autosave every 5 minutes in workshop mode.

Existing users, that have Creation Club content installed will need to browse to the installation folder, and delete the "mods" folder before installing this update. Once the update is installed, re-run the Creation Organizer to ensure all appropriate Creation Club and Creation Club using addons are enabled correctly.

You should refresh all plots in your settlements.

## 3.25.0

**Released:** `27 Sep 2023`

### Info <!-- omit in toc -->

- The SS2CPC Helper now supports both Steam and GoG releases of Fallout 4.
- Installation size has been reduced from 50GB to 15GB. 35GB saved!
- Updated to the most recent release of SimSettlements, and supported addons.
- It is intentionally not possible to edit the load order to add additional mods.
- Supported Creation Club content is now automatically enabled. (Technical limitations)
- Creation Organizer now only enables addons that depend on CC content.
- Creation Organizer does not work with GoG installations. (They don't have Creation Club).
- Startup and shutdown are slower, as it's now backing up and restoring files in your main Fallout 4 installation.
- Applying Yagisan's City Plan Contest MCM Settings will enable an autosave every 5 minutes in workshop mode.

Existing users, that have Creation Club content installed will need to browse to the installation folder, and delete the "mods" folder before installing this update. Once the update is installed, re-run the Creation Organizer to ensure all appropriate Creation Club and Creation Club using addons are enabled correctly.

You should refresh all plots in your settlements.

## 3.24.2

**Released:** `14 Jun 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - June 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using Tarsis31 and Yagisan's Lakeside Cabin Settlement.](https://www.nexusmods.com/fallout4/mods/35553)**

This release contains an updated **[Sim Settlements 2 Addon Pack Caravan Snatex](https://www.nexusmods.com/fallout4/mods/63578)**. This has navmesh fixes for all plots.

Consider refreshing any plots from this pack.

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.


## 3.24.1

**Released:** `9 June 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - June 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using Tarsis31 and Yagisan's Lakeside Cabin Settlement.](https://www.nexusmods.com/fallout4/mods/35553)**

This release contains an updated **[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)**. This has script spawn fixes that should automatically take affect when you enter the settlement.

This release contains an updated **[Wasteland Venturers Sim Settlements 2 Addon Pack](https://www.nexusmods.com/fallout4/mods/48060)**. This has plot build, and plot crashing fixes.

Consider refreshing your plots.

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.24.0

**Released:** `31 May 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - June 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using Tarsis31 and Yagisan's Lakeside Cabin Settlement.](https://www.nexusmods.com/fallout4/mods/35553)**

This release contains an updated **[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** release that is not available on the Nexus. Entrants should use this version to export their plans.

**[DXVK](https://github.com/doitsujin/dxvk)** has been updated to 2.2 - If you are having video errors or crashes, uncheck it in the MO2 menu. For optimal results use your monitors native resolution. For many people it provides a performance boost.

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.23.1

**Released:** `20 May 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - May 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using Glichfinder's North Point Park Settlement.](https://www.nexusmods.com/fallout4/mods/70410)**

This release contains an updated **[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** release that is not available on the Nexus. Entrants should re-export their plans, and release updated plans to the Nexus.

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.23.0

**Released:** `1 May 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - May 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using Glichfinder's North Point Park Settlement.](https://www.nexusmods.com/fallout4/mods/70410)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.22.2

**Released:** `15 Apr 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - April 2023 Contest.

Rusty Face Fix can be switched between the old (1.2.x) and new (2.0.x) releases. Use the old Rusty Face Fix to load save files made with old versions of the SS2CPC Helper to avoid crashes.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using XV-Versus and Yagisan's Ruined Church Settlement.](https://www.nexusmods.com/fallout4/mods/70005)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.22.1

**Released:** `15 Apr 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - April 2023 Contest.

**This release contains an alpha release of Workshop Framework that correctly exports the settlement location.**

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using XV-Versus and Yagisan's Ruined Church Settlement.](https://www.nexusmods.com/fallout4/mods/70005)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.22.0

**Released:** `1 Apr 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - April 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using XV-Versus and Yagisan's Ruined Church Settlement.](https://www.nexusmods.com/fallout4/mods/70005)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.21.1

**Released:** `7 Mar 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - March 2023 Contest.

**This is an emergency hotfix release. Due to an infinite loop bug in Sim Settlements 2, version 2.3.2 all saves made in the SS2CPC Helper 3.21.0 are broken. You will need to restart your entry.**

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using XV-Versus and Yagisan's Crater of Atom Settlement.](https://www.nexusmods.com/fallout4/mods/67788)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.21.0

**Released:** `5 Mar 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - March 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This is a special release - **[We are using XV-Versus and Yagisan's Crater of Atom Settlement.](https://www.nexusmods.com/fallout4/mods/67788)**

To install and enable optional Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

## 3.20.4

**Released:** `27 Feb 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - February 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release now includes a tool to collect all relevant logs to help with technical support with this list. After exiting Fallout 4 (or right after it crashes), select **Yagisan's Log Grabber** from the menu bar where you see **F4SE**. Select run. It will do its thing, and provide you with a zip file that you can upload for support.

This is a special release - **[We are using the Fairline Hills Settlement by Pra.](https://www.nexusmods.com/fallout4/mods/35869)**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**Workshop Framework** was updated to a beta release to correctly export the settlement.

## 3.20.3

**Released:** `21 Feb 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - February 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release now includes a tool to collect all relevant logs to help with technical support with this list. After exiting Fallout 4 (or right after it crashes), select **Yagisan's Log Grabber** from the menu bar where you see **F4SE**. Select run. It will do its thing, and provide you with a zip file that you can upload for support.

This is a special release - **[We are using the Fairline Hills Settlement by Pra.](https://www.nexusmods.com/fallout4/mods/35869)**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[Fairline Hills Settlement](https://www.nexusmods.com/fallout4/mods/35869)**  scrapped building parts will no longer magically come back in your plans. You must remake all exports. Sorry.

**Sim Settlements 2 and several addons** were updated for the March contest. As this is a fix late in the February contest, and I had already prepared for next month, I didn't roll them back.

## 3.20.2

**Released:** `12 Feb 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - February 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release now includes a tool to collect all relevant logs to help with technical support with this list. After exiting Fallout 4 (or right after it crashes), select **Yagisan's Log Grabber** from the menu bar where you see **F4SE**. Select run. It will do its thing, and provide you with a zip file that you can upload for support.

This is a special release - **[We are using the Fairline Hills Settlement by Pra.](https://www.nexusmods.com/fallout4/mods/35869)**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[City Plan Contest Assistant](https://www.nexusmods.com/fallout4/mods/50366)** no longer flags Fairline Hills as invalid. Whoops.

**[F4SE Garbage Collector Fix](https://www.nexusmods.com/fallout4/mods/68681)** now uses the Nexus download location, as it's finally posted there.

## 3.20.1

**Released:** `5 Feb 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - February 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release now includes a tool to collect all relevant logs to help with technical support with this list. After exiting Fallout 4 (or right after it crashes), select **Yagisan's Log Grabber** from the menu bar where you see **F4SE**. Select run. It will do its thing, and provide you with a zip file that you can upload for support.

This is a special release - **[We are using the Fairline Hills Settlement by Pra.](https://www.nexusmods.com/fallout4/mods/35869)**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[DXVK](https://github.com/doitsujin/dxvk)** has been updated to 2.1 - This contains performance increases, and workarounds for bugs in AMD Vulkan drivers.

## 3.20.0

**Released:** `29 Jan 2023`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - February 2023 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release has had **[DXVK](https://github.com/doitsujin/dxvk)** integrated. As a result you now require the latest Vulkan graphics drivers for your GPU. This will be part of the latest release of your graphics drivers - please update them. DXVK integration has been tested over December and January, and shown to improve performance in many cases.

This is a special release - **[We are using the Fairline Hills Settlement by Pra.](https://www.nexusmods.com/fallout4/mods/35869)**

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[SS2 Industrial Revolution of the Wasteland (Add-on Pack)](https://www.nexusmods.com/fallout4/mods/65545)** updated to 5.0

**[IT2 4 SS2](https://www.nexusmods.com/fallout4/mods/65273/)** updated to 2.0.0

**[Wasteland Venturers Sim Settlements 2 Addon Pack](https://www.nexusmods.com/fallout4/mods/48060)** updated to 1.5.0

**[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)** updated to 15.0.0

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 2.2.0

**[Sim Settlements 2 - Far Harbor Expansion](https://www.nexusmods.com/fallout4/mods/61661)** updated to 2.0

**[Captain Cosmos Creation V2 - A Sim Settlements 2 Plot pack](https://www.nexusmods.com/fallout4/mods/48233)** updated to 2.0

### Additions <!-- omit in toc -->

**[Sim Settlements AddonPack - Awsometown](https://www.nexusmods.com/fallout4/mods/27384)**

**[Powerful Plots for Superlative Settlers - A Sim Settlements 2 Add-on Pack](https://www.nexusmods.com/fallout4/mods/67406)**

**[SS2 Support Structures of the Wasteland (Add-on Pack)](https://www.nexusmods.com/fallout4/mods/67522)**

## 3.19.3

**Released:** `2 Nov 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - November 2022 Contest.

This is a special release - for the first time ever, the contest is officially using a mod added settlement. **[We are using the Mystic Pines Redux by fftfan / XV-Versus.](https://www.nexusmods.com/fallout4/mods/39372)**

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 2.0.2

## 3.19.2

**Released:** `30 Oct 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - November 2022 Contest.

This is a special release - for the first time ever, the contest is officially using a mod added settlement. **[We are using the Mystic Pines Redux by fftfan / XV-Versus.](https://www.nexusmods.com/fallout4/mods/39372)**

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.4a

## 3.19.1

**Released:** `29 Oct 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - November 2022 Contest.

This is a special release - for the first time ever, the contest is officially using a mod added settlement. **[We are using the Mystic Pines Redux by fftfan / XV-Versus.](https://www.nexusmods.com/fallout4/mods/39372)**

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Additions <!-- omit in toc -->

**[SS2 Industrial Revolution of the Wasteland (Add-on Pack)](https://www.nexusmods.com/fallout4/mods/65545)**

## 3.19.0

**Released:** `29 Oct 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - November 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[City Plan Contest Assistant](https://www.nexusmods.com/fallout4/mods/50366)** updated to 2.2.4.

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.3.1

**[Workshop Plus](https://www.nexusmods.com/fallout4/mods/35005)** updated to 1.0.12

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.4

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.2.4

**[Sim Settlements 2 Wasteland Reconstruction Kit](https://www.nexusmods.com/fallout4/mods/48960)** updated to 0.2

**[Sim Settlements 2 Scrappers](https://www.nexusmods.com/fallout4/mods/48846)** updated to 5.7

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 2.0.1

**[Sim Settlements 2 Settlement Management Terminal](https://www.nexusmods.com/fallout4/mods/64135)** updated to 1.3

### Additions <!-- omit in toc -->

**[Immersive Teleportation 2](https://www.nexusmods.com/fallout4/mods/35109)**

**[IT2 4 SS2](https://www.nexusmods.com/fallout4/mods/65273/)**

**[Sim Settlements 2 - From Sanctuary to Concord - Building Plans Module](https://www.nexusmods.com/fallout4/mods/62210)**

## 3.18.1

**Released:** `4 Oct 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - October 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[City Plan Contest Assistant](https://www.nexusmods.com/fallout4/mods/50366)** updated to 2.2.2a hotfix. Updated version will force open the Mech Lair door on any **new** saves.

**[LOOT](https://github.com/loot/loot)** updated to 0.18.5

**[Pra's Fo4Edit Scripts](https://www.nexusmods.com/fallout4/mods/28898)** updated to 1.31

**[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)** updated to 14.0.0

## 3.18.0

**Released:** `29 Sep 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - October 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**New Creation Club based addons are included. You must re-run the instructions below to enable it.**

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.4

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.2

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.2.2a

**[Sim Settlements 2 Addon Pack Caravan Snatex](https://www.nexusmods.com/fallout4/mods/63578)** updated to 1.2.0

**[Sim Settlements 2 - Addon Pack - DZK Concrete Defensible Positions](https://www.nexusmods.com/fallout4/mods/61435)** updated to 1.2.2

### Additions <!-- omit in toc -->

**[This Settlement Does Not Need Your Help - BS Defence Redone](https://www.nexusmods.com/fallout4/mods/63998)**

**[Choochoo1's Neon Bar Sim Settlements 2 Edition](https://www.nexusmods.com/fallout4/mods/64561)** ESL version.

**[Sim Settlements 2 Settlement Management Terminal](https://www.nexusmods.com/fallout4/mods/64135)** provides a useful terminal that shows who is homeless, unemployed, need a hobby etc. **It is not competition legal and you must scrap it before exporting.**

### Removed <!-- omit in toc -->

**[BS Defence - This Settlement Does Not Need Your Help](https://www.nexusmods.com/fallout4/mods/20137)** deleted upstream

## 3.17.0

**Released:** `29 Aug 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - September 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

This release now can **optionally** install the following Creation Club Content, if it is detected.

 - Arcade Workshop Pack
 - Charlestown Condo
 - Coffee and Donuts Workshop Pack
 - Home Decor Workshop Pack
 - Modern Furniture Workshop Pack
 - Nuka-Cola Collector Workshop
 - Noir Penthouse
 - Holiday Workshop Pack
 - Shroud Manor
 - Neon Flats
 - Capital Wasteland Mercenaries
 - Captain Cosmos
 - Settlement Ambush Kit

Players must obviously own that Creation Club content, **and** must have downloaded it via the in-game launcher, in their main Fallout 4 installation - not in a SS2CPC Helper installation.

To install and enable the Creation Club content, click on the jigsaw puzzle icon in the menu bar. Then select `Creation Organizer`. Then restart the SS2CPC Helper. You should do this after you download new Creation Club content, to get changes and updates.

**Please note that Creation Club content is currently forbidden in the Sim Settlements City Plan Contest.** Plots that use Creation Club content are permitted.

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.3

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.1

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.2.1

### Additions <!-- omit in toc -->

**[Captain Cosmos Creation V2 - A Sim Settlements 2 Building](https://www.nexusmods.com/fallout4/mods/48233)** This will automatically enable only if you own the Captain Cosmos CC content.

**[Sim Settlements 2 Addon Pack Caravan Snatex](https://www.nexusmods.com/fallout4/mods/63578)**

**[Elevator Buttons Fix (Contraptions)](https://www.nexusmods.com/fallout4/mods/20664)** if your elevator buttons bug out, fast travel away from the settlement and back. I suggest to vault 111 and back.

**[NSO - New Snap Order - snap points for furniture and decor](https://www.nexusmods.com/fallout4/mods/13959)** Additional snappoints. Enable if wanted.

**[Wasteland Workshop Snappable Posters](https://www.nexusmods.com/fallout4/mods/62564)** Additional snappoints. Enable if wanted.

**[Ummersive Snappy Stairs](https://www.nexusmods.com/fallout4/mods/62534)** Additional snappoints. Enable if wanted.

**[Useful Wooden Railings](https://www.nexusmods.com/fallout4/mods/61850)** Additional snappoints. Enable if wanted.

**[Snappy Corridors(Outer Walls](https://www.nexusmods.com/fallout4/mods/61770)** Additional snappoints. Enable if wanted.

**[Useful Posts](https://www.nexusmods.com/fallout4/mods/61294)** Additional snappoints. Enable if wanted.

**[Warehouse Top Wall Snap](https://www.nexusmods.com/fallout4/mods/61268)** Additional snappoints. Enable if wanted.

**[Snappy Half Walls](https://www.nexusmods.com/fallout4/mods/61248)** Additional snappoints. Enable if wanted.

**[Garden Plot Snap](https://www.nexusmods.com/fallout4/mods/61193)** Additional snappoints. Enable if wanted.

**[Scaffolding Snapping](https://www.nexusmods.com/fallout4/mods/61017)** Additional snappoints. Enable if wanted.

**[Warehouse Corner Wall Snap](https://www.nexusmods.com/fallout4/mods/60955)** Additional snappoints. Enable if wanted.

## 3.16.2

**Released:** `31 Jul 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - August 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**You MUST reapply the contest settings in the MCM after this update**

### Updates <!-- omit in toc -->

**[Sim Settlements 2 Scrappers](https://www.nexusmods.com/fallout4/mods/48846)** updated to 5.5

**[Plain Plans by MsB - SS2 Add-On Pack](https://www.nexusmods.com/fallout4/mods/62383)** updated to 1.1

## 3.16.1

**Released:** `31 Jul 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - August 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

**You MUST reapply the contest settings in the MCM after this update**

### Updates <!-- omit in toc -->

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.0b

## 3.16.0

**Released:** `29 Jul 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - August 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.2

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.2.0a

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.2.0

**[Sim Settlements 2 Scrappers](https://www.nexusmods.com/fallout4/mods/48846)** updated to 5.4

**[Unofficial Fallout 4 Patch](https://www.nexusmods.com/fallout4/mods/4598)** updated to 2.1.4

### Additions <!-- omit in toc -->

**[Sim Settlements 2 - Far Harbor Expansion](https://www.nexusmods.com/fallout4/mods/61661)**

**[Plain Plans by MsB - SS2 Add-On Pack](https://www.nexusmods.com/fallout4/mods/62383)**

## 3.15.2

**Released:** `10 Jul 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - July 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

Based on data gathered so far in the July 2022 Contest, the build limit calculator in the City Plan Contest has been further refined. **Please rerun this tool as the calculations have changed.** In addition to showing the build limit used, it now creates a `SS2_ContestBuildLimitUsage.0.log` log file with detailed logs of what is using up your build limit.

### Updates <!-- omit in toc -->

**[High FPS Physics Fix](https://www.nexusmods.com/fallout4/mods/44798)** updated to 0.8.6

## 3.15.1

**Released:** `1 Jul 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - July 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

Now includes a batch file to supply you components to help jumpstart plot building. Open the console, and ran `bat build` to spawn a bunch of components. Store them in the workshop.

## 3.15.0

**Released:** `30 Jun 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 - July 2022 Contest.

You **MUST** use the supplied `CleanSaveVault.fos` or `New_Game_V111_Exit__Yagisan.fos` saves to create your entry.

### Additions <!-- omit in toc -->

**[Sim Settlements 2 - Addon Pack - DZK Concrete Defensible Positions](https://www.nexusmods.com/fallout4/mods/61435)**

### Updates <!-- omit in toc -->

**[F4SE](https://f4se.silverlock.org/)** updated to 0.6.23

**[Buffout 4](https://www.nexusmods.com/fallout4/mods/47359)** updated to 1.26.2

**[High FPS Physics Fix](https://www.nexusmods.com/fallout4/mods/44798)** updated to 0.8.5

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 2.0.0

**[SS2 - Settlers at Play](https://www.nexusmods.com/fallout4/mods/60443)** updated to 0.2

**[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)** updated to 13.1.1

## 3.14.4

**Released:** `7 Jun 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 Masters Contest.

You **MUST** use the supplied `Masters2022Save.fos` save to create your entry.

### Additions <!-- omit in toc -->

**[Happy Trails - Sim Settlements 2 Addon Pack](https://www.nexusmods.com/fallout4/mods/50835)** custom stores fixed in 1.1

### Updates <!-- omit in toc -->

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.1.3b

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.1.3a

**[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)** updated to 12.1.1

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 1.9.0

**[Sim Settlements 2 - Ruined Homes and Gardens](https://www.nexusmods.com/fallout4/mods/48067)** updated to 1.2.0

**[MCM Settings Manager](https://www.nexusmods.com/fallout4/mods/56195)** updated to 1.1

### Removed <!-- omit in toc -->

**[Power Grid Tools](https://www.nexusmods.com/fallout4/mods/17777)** obsolete with Workshop Framework

## 3.14.3

**Released:** `15 May 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 Masters Contest.

You **MUST** use the supplied `Masters2022Save.fos` save to create your entry.

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.1a

## 3.14.2

**Released:** `14 May 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 Masters Contest.

You **MUST** use the supplied `Masters2022Save.fos` save to create your entry.

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** plots need to be refreshed after this update. You can do this from the ASAM.

### Additions <!-- omit in toc -->

**[SS2 - Settlers at Play](https://www.nexusmods.com/fallout4/mods/60443)**

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.1

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.1.3

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.1.3

**[Jampads 2 - a Sim Settlements 2 Add-on](https://www.nexusmods.com/fallout4/mods/48618)** updated to 1.8.0

**[Sim Settlements 2 - Rags and Riches](https://www.nexusmods.com/fallout4/mods/58189)** updated to 2.0.0

## 3.14.1

**Released:** `30 Apr 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 Masters Contest.

You **MUST** use the supplied `Masters2022Save.fos` save to create your entry.

### Updates <!-- omit in toc -->

**[Workshop Framework](https://www.nexusmods.com/fallout4/mods/35004)** updated to 2.2.0

**[Sim Settlements 2](https://www.nexusmods.com/fallout4/mods/47976)** updated to 2.1.2

**[Sim Settlements 2 - Chapter 2](https://www.nexusmods.com/fallout4/mods/55817)** updated to 2.1.2

## 3.14.0

**Released:** `29 Apr 2022`

### Info <!-- omit in toc -->

This is for the Sim Settlements Season 3 Masters Contest.

You **MUST** use the supplied `Masters2022Save.fos` save to create your entry.

### Updates <!-- omit in toc -->

**[Vault-Tec Tools - Sim Settlements 2 Addon Pack](https://www.nexusmods.com/fallout4/mods/48700)** updated to 1.0.5a

**[Sim Settlements 2 - Pra's Random Addon 2](https://www.nexusmods.com/fallout4/mods/48042)** updated to 12.0.0

## 3.13.2

**Contest: April 2022** 

**Released:** `23 Apr 2022`

### Info <!-- omit in toc -->

This is a pre-release of Sim Settlements 2 City Plan Contest Helper. It is subject to change, and should not be used for a non-testing entry.

### Additions <!-- omit in toc -->

**Yagisan's Workshop Unlocker** unlocks most buildable items (Main Quest items excluded)

### Updates <!-- omit in toc -->

### Removed <!-- omit in toc -->

**[Happy Trails - Sim Settlements 2 Addon Pack](https://www.nexusmods.com/fallout4/mods/50835)** discovered to break custom stores.


## 3.13.1

**Contest: April 2022** 

**Released:** `22 Apr 2022`

### Info <!-- omit in toc -->

This is a pre-release of Sim Settlements 2 City Plan Contest Helper. It is subject to change, and should not be used for a non-testing entry.