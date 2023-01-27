# How to use SVRP

## Preparations
First, copy all the patchable (.sny and .mod) files from your recovery partition or discs using [this guide](https://github.com/Vir0z4/svrp/wiki/How-to-find-.sny-and-.mod-files). 
If you do not have .sny files (which are the most important), your recovery partition or discs aren't supported yet. If you don't have .mod files, but only .sny files, you can continue.

**Make sure that you copied all the files to a writable folder which path contains no spaces!** (example: "C:\patchfiles")

If you're having any issues when using SVRP, please see the [Troubleshooting](Troubleshooting.md) page.

## Installing SVRP

Download the [latest release](https://github.com/Vir0z4/svrp/releases/latest) of SVRP. Proceed with the installation.

**Make sure you are installing SVRP in the default directory** (C:\SVRP), otherwise SVRP will not work.

## Using SVRP for .sny files (Windows installation)

* Start the program. Click on `.sny`.

* After that, you will be asked to enter input folder, which is the folder that contains all the .sny files, an output folder, which is where the WIM will be saved, and name of the first .sny file (usually has the shortest name, like "sony.sny" or "p2.sny"). You also need to enter the file extension.

* Click on `Patch`, and process 1 will start. This process usually takes around 2-3 seconds.

* Press enter to continue with process 2.

* If process 2 succeded without errors, you should now find your WIM file in the output directory.

**To learn more on how to install the WIM file (Windows), please visit [this page](How-to-install-WIM-files.md).**

## Using SVRP for .mod files (applications)

Please only extract .mod files after installing Windows.

* Make sure that all the names of .mod files **don't contain spaces**.

* Start the program. Click on `.mod`. You will then have 2 options, automatic patcher, and manual patcher. If you want to extract multiple .mod files, it is recommended to use the automatic patcher. If you want to extract one .mod file at a time, use the manual patcher.

* You will be asked to enter input folder, which is the folder that contains all the .mod files, and an output folder, which is where the .mod files will be extracted. For the manual patcher, you also need to enter the full name of the .mod file you desire to patch (example: "MODJ-164418.mod").

* Click on `Auto extract`, or `Extract` for manual patcher, and process 1 will start. This process usually takes around 2-3 seconds.

* Press enter to continue with the next file (auto patcher). Press enter to continue with process 2 (manual patcher).

* If process 2 succeded without errors, the extracted .mod should be in the output folder.

**Install applications using the guide on the [Post-installation](Post-installation.md) page.**
