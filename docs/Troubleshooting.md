# Troubleshooting

For support, please join the [Sony MegaServer](https://discord.gg/EdccRK73nC) Discord server and talk to us on the #vaio channel.

## Errors while running SVRP

### Process 1: `Write failed`

This problem happens because the file is in read-only, and SVRP failed to remove the attribute. To fix this issue, right click on the patchable file, go to `Properties`, and uncheck `Read-Only`. Then click on `Apply`.

### Process 1: `Read failed`

This means that the directory or file was not found. **Please check that the path and file contains no spaces** (path example: "C:\patchfiles") (file example: "MOD-WinDVD.mod"), and you entered the correct "first file" (for .sny files), **with file extension** (example: "sony.sny", or "p2.sny").

### Process 2: `The file did not begin with the magic characters that identify a WIM file`

This error usually means that process 1 failed, or you inputted the wrong "first file". Please try again, and check what error you obtain on process 1.

## Errors when installing the WIM (Windows)

### `The subsystem needed to support the image type is not present`

To install x64 WIMs (some older recoveries contain 32-bit Windows, and newer ones, 64-bit), you need the x64 version of wimlib-imagex. Using the x64 version should fix this problem.

### `This version of wimlib-imagex.exe is not compatible with the version of Windows you're running`

If you are currently using wimlib-imagex "windows-i686-bin", which is the 32-bit version, switch to the "windows-x86_64-bin", which is the 64-bit, and vice-versa.

## Errors on first boot (Windows)

**If you can see a BSOD at boot, but can't get a grasp of what it's saying, record a video using your phone, then stop on a frame with the BSOD.**

### BSOD: `Windows did not find any installed, licensed language packs for the system default UI language (0x0000012a)`

**This problem happens on nearly all Windows 7 recoveries.** Sometimes, the BSOD doesn't show at all, and the system simply reboots, however, this method should fix it.

Please see [the page](https://github.com/Vir0z4/svrp/wiki/BSOD:-Windows-did-not-find-any-installed,-licensed-language-packs-for-the-system-default-UI-language-(0x0000012a)) dedicated to this problem.
