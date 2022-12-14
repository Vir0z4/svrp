# Sony VAIO Recovery Patcher (SVRP)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vir0z4/svrp)
![GitHub all releases](https://img.shields.io/github/downloads/vir0z4/svrp/total)
![GitHub issues](https://img.shields.io/github/issues/vir0z4/svrp)
![GitHub](https://img.shields.io/github/license/vir0z4/svrp)

### Batch version

*SVRP* is a utility designed to patch and combine split WIM (.wim) files from Sony VAIO recoveries, **in order to bypass Sony's model checks**. This tool can be used when the recovery discs refuse to install, as they were not made on the unit they are trying to be installed on.

**A GUI version with support for other files is coming soon. For now, please use the batch version.**

The batch version supports **.sny** and **.mod** files only, for now. Please visit the [wiki](https://github.com/Vir0z4/svrp/wiki/How-to-find-.sny-and-.mod-files) to learn how to find .sny and .mod files.

## Documentation

Please visit the [wiki](https://github.com/Vir0z4/svrp/wiki). **It is important to read the documentation before using SVRP!**

SVRP must be installed and used in an environment with paths **that do not contain spaces!** Must be ran from executable, not batch file!

For support, please join the [Sony MegaServer](https://discord.gg/EdccRK73nC) Discord server and talk to us on the #vaio channel.

## Miscellaneous Informations

The SVRP executable (SVRP.exe) is the batch file (SVRP.bat) converted to executable using "[Bat to Exe Converter](https://www.f2ko.de/programme/bat-to-exe-converter/)" by F2KO. This convertion is what makes some antiviruses think that SVRP is a virus.

[wimlib-imagex](https://wimlib.net) (version 1.13.6) is the tool of choice for exporting and extracting WIMs. It is used over Microsoft's ImageX as it offers more functionality, stability, and has a considerably higher success rate.

Sony Vaio MOD Patcher (patchmod.exe) is used to patch .sny and .mod files, in order for wimlib-imagex to be able to recognize them. Original source of this program is currently unknown, as it was originally published on the now defunct NotebookReview forums.

This patching method was discovered by a NotebookReview forum user named "madurai_tiger". Download link to the original tool [here](https://drive.google.com/file/d/1YD7bDr-aW9nuFUKLNVEx94GMLfDBNo_b/view?usp=sharing). The original tool is not automated, and it fails to put together some split WIM files correctly, as it uses Microsoft's ImageX instead of the better wimlib-imagex.
