# Sony VAIO Recovery Patcher (SVRP)
![GitHub all releases](https://img.shields.io/github/downloads/vir0z4/svrp/total)
![GitHub issues](https://img.shields.io/github/issues/vir0z4/svrp)
![GitHub](https://img.shields.io/github/license/vir0z4/svrp)

### Batch version

*SVRP* is a utility designed to patch and combine split WIM (.wim) files from Sony VAIO recoveries, in order to bypass Sony's model checks. This tool can be used when the recovery discs refuse to install, as they were not made on the unit they are trying to be installed on.

**A GUI version with more support for other files such as .mod is coming soon. For now, please use the batch version.**

The batch version supports .sny files ONLY (for now)!

## Documentation

Please visit the [wiki](https://github.com/Vir0z4/svrp/wiki).

## License Informations

This open-source program is distributed under the GPL-3.0 license. It is required to follow the license, we will not hesitate to take legal action if the license is not followed.

## Miscellaneous Informations

The SVRP executable (SVRP.exe) is the batch file (SVRP.bat) converted to executable.

[wimlib-imagex](https://wimlib.net) (version 1.13.6) is the tool of choice for putting together the split WIM files. It is used over Microsoft's ImageX as it offers more functionality, stability, and has a considerably higher success rate.

Sony Vaio MOD Patcher (patchmod.exe) is used to patch the the first split WIM file, in order for wimlib-imagex to be able to put the full WIM together. It is also used to patch .mod files. Original source of this program is currently unknown, as it was originally published on the now defunct NotebookReview forums.

This patching method was discovered by a NotebookReview forum user named "madurai_tiger". Download link to the original tool [here](https://drive.google.com/file/d/1YD7bDr-aW9nuFUKLNVEx94GMLfDBNo_b/view?usp=sharing). The original tool does not have a GUI, and it fails to put together some split WIM files correctly, as it uses Microsoft's ImageX instead of the better wimlib-imagex.
