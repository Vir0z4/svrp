# How to install WIM files

## Preparations

First, you need a Windows PE environment that you can run on the target machine (Windows ISOs, etc...). 

You then need a copy of [wimlib-imagex](https://wimlib.net) (we recommend the "windows-x86_64-bin" version for maximum compatibility). Extract the program, then copy it over to the root of your PE environment media, or on another USB drive or media.

Then, copy over the WIM file SVRP created to the wimlib-imagex folder you just transferred to your PE environment media, or on another USB drive or media.

If you're having any issues, please see the [Troubleshooting](Troubleshooting.md) page.

## Windows 7 recoveries

To install Windows 7 recoveries, you must go through with [this guide](BSOD_0x0000012a.md) **before installing the WIM**. Only for Windows 7.

## Initial setup

* First, boot into the PE environment on the target machine, and enter the command prompt (using Shift+F10 or "Repair your computer").

* Type `diskpart`

* Then `list disk`

* Find the number of the disk you want to install the WIM on.

* Then, type `select disk (disk number)`

* Type `clean` (THIS WILL WIPE ALL DATA ON DISK)

* Type `create partition primary`

* Type `format fs=ntfs quick`

* Type `assign letter=C` (if C is already assigned, deassign the other partition that is currently assigned C, using `select volume (enter number)` and `remove letter=c`, then select the partition we were creating and assign it C)

* Type `active`

* Type `exit`

## Applying the WIM

* Find the drive letter of whatever media you transferred wimlib-imagex to (using diskpart, or notepad). To switch drive letter on CMD, simply type `(drive letter):`

* Navigate to the area where you transferred wimlib-imagex with the command `cd (path)`

* To start the installation, execute the command `wimlib-imagex.exe apply (name).wim 1 C:`

Then, to create the boot files, you must use this command:

* `bcdboot.exe C:\Windows /s C:\`

If the command is unknown, use a Windows 10 PE.

**Proceed to [Post-installation](Post-installation.md) guide.** For BSOD issues related to language packs, etc, please see the [Troubleshooting](Troubleshooting.md) page.
