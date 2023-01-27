# Post-installation

## Warning

**Please make sure to follow the instructions on this page.**

## First boot

**For BSOD issues** related to language packs, etc, please see the [Troubleshooting](Troubleshooting.md) page.

After Windows has been successfully installed, let it get to the Desktop. 

If it restarts into OOBE without any input from your part, you must go through with OOBE and install the applications after (how-to below). 
**If it does not restart into OOBE**, install the applications, and then you should be able to find a Sysprep window, click on restart.

## Information about applications

Sometimes, all applications are already installed, sometimes, only some are installed, and sometimes, none are installed.

If not all are installed, you must install them by extracting .mod files.

**If you are not sure if all apps are installed**, please extract a couple of .mod files (preferably the biggest), and check if these apps are installed.

Please only install the apps that are not installed, don't reinstall ones that are already installed.

## How to install applications (.mod files)

* First, extract all the .mod files using SVRP. Please see the guide on [how to use SVRP](How-to-use-SVRP-GUI.md).

* Put the extracted .mod files on a USB drive or other removable media.

* Install each .mod file one by one by going through `setup.exe` and `setup.bat`. **Each time, make sure to run the setup executables and batch files as Administrator!**

## Drivers

If some drivers are missing, even after installing all .mod files, you must download and install them manually. 

To find and download drivers, you can use a guide such as [this one](https://vaiolibrary.com/index.php/Download_drivers_using_sonyvaiodriver.com_and_a_copy_of_ftp.vaio-link.com).
