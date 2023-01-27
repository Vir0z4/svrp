# How to find .sny and .mod files

## Preparations

Please mount your recovery partition, insert your recovery discs, or extract ISOs (using 7-Zip or Win-RAR).

For Windows 7 users, disable `Hide extensions for known file types`, and for Windows 8/8.1/10/11 users, enable `File name extensions`.

## Getting .sny files

**.sny files contain the WIM (Windows installation).**

On some recoveries, you can find them on the root directory, but on others, they are hidden in the "data" folder.

**In order to find them quickly**, use the "Search" function on Windows Explorer, simply by typing `.sny` (make sure to check **all** discs!). 
Then, copy all the files to a **writable folder which path does not contain spaces**.

Make sure to not confuse .sny files with files that contain sny in the name! We only want the files with the `.sny` file extension (for example "sony.sny", **not** "SNYHDRCV.dll").

**Sometimes no .sny files can be found on the first recovery disc**, but can be found on the second, third, or vice versa. 

If no .sny files can be found, your recovery is not yet supported.

**Please continue with the guide on [how to use SVRP](How-to-use-SVRP-GUI.md).**

## Getting .mod files

**.mod files contain applications.**

Sometimes, .mod files are already bundled inside .sny files. **So before taking care of .mod files, please extract the WIM from .sny files and install Windows.**

**In order to find .mod files**, use the "Search" function on Windows Explorer, simply by typing `.mod` (make sure to check **all** discs!). 
Then, copy all desired files to a **writable folder which path does not contain spaces**.

Make sure to not confuse .mod files with files that contain mod in the name! We only want the files with the `.mod` file extension (for example "MODJ-164441.mod", **not** "MODSYSAP.dll").

These files sometimes have random names, or are named after the application inside. Both are equally important.

If you do not have any .mod files, but have .sny files, you can use SVRP.

Check [Post-installation](Post-installation.md) guide for more information on applications.

**Please continue with the guide on [how to use SVRP](How-to-use-SVRP-GUI.md).**
