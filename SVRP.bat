ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (SVRP)

ECHO Sony VAIO Recovery Patcher (SVRP)
ECHO 2022 - Vir0z4 Network IT
ECHO.
ECHO This tool supports .sny files ONLY (for now)!
ECHO.
ECHO Make sure the folder with patchable files is writable, path contains NO spaces, and contains only the .sny files you want to patch!
ECHO.
PAUSE

CLS
SET /p "inputfolder=Copy and paste path to folder with patchable files: "
ECHO.
SET /p "f2=Enter name of first .sny file (usually has the shortest name) (example: sony.sny): "

ECHO Process 1 started...
START /B /WAIT %cd%\patchmod.exe %inputfolder%\%f2%
ECHO.
ECHO Process 1 completed. 
ECHO Please check in explorer if the first .sny file was modified (date modified). If it was modified at the current time, continue.
PAUSE

CLS
ECHO Process 2 started...
ECHO.
START /B /WAIT cmd /c "%cd%\wimlib-imagex\wimlib-imagex.exe export %inputfolder%\%f2% 1 %inputfolder%\sony.wim "Sony" --ref="%inputfolder%\*.sny""
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO.
ECHO The WIM file should now be in the folder with patchable files!
ECHO For more information on how to install this WIM file, please follow the documentation on the SVRP GitHub repository.

PAUSE