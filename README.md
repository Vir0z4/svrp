# Sony VAIO Recovery Patcher (SVRP)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vir0z4/svrp)
![GitHub all releases](https://img.shields.io/github/downloads/vir0z4/svrp/total)
![GitHub issues](https://img.shields.io/github/issues/vir0z4/svrp)
![GitHub](https://img.shields.io/github/license/vir0z4/svrp)

### GUI version

*SVRP* is a utility designed to patch and combine split WIM (.sny) and .mod files from Sony VAIO recoveries, **in order to bypass Sony's model checks**. This tool can be used when the recovery discs refuse to install, as they were not made on the unit they are trying to be installed on.

It can patch **.sny** files, which contain the Windows installation in form of a WIM, and **.mod** files, which are applications (most of the VAIO apps, and others).

![SVRP GUI Screenshot](https://i.postimg.cc/Bvpbcvs0/SVRP-main-crop.png)

The GUI version is **easier and faster to use** compared to the batch version, and it features an auto .mod patcher which detects all the .mod files in a folder, and automatically patches all of them.

## Documentation

**Please visit the [documentation](https://svrp.vir0z4.com).**

SVRP must be installed in the default location (C:\SVRP) and used in an environment with paths **that do not contain spaces!**

For support, please join the [Sony MegaServer](https://discord.gg/EdccRK73nC) Discord server and talk to us on the #vaio channel.

## Miscellaneous Informations

This tool was developed with Python and batch, and was packaged to a standalone exe by Nuitka.

[wimlib-imagex](https://wimlib.net) (version 1.13.6) is the tool of choice for exporting and extracting WIMs. It is used over Microsoft's ImageX as it offers more functionality, stability, and has a considerably higher success rate.

Sony Vaio MOD Patcher (patchmod.exe) is used to patch .sny and .mod files, in order for wimlib-imagex to be able to recognize them. Original source of this program is currently unknown, as it was originally published on the now defunct NotebookReview forums.

This patching method was discovered by a NotebookReview forum user named "madurai_tiger". Download link to the original tool [here](https://drive.google.com/file/d/1YD7bDr-aW9nuFUKLNVEx94GMLfDBNo_b/view?usp=sharing). The original tool is not automated, and it fails to put together some split WIM files correctly, as it uses Microsoft's ImageX instead of the better wimlib-imagex.
