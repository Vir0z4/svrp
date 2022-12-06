ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (SVRP)

:MENU
CLS
ECHO Sony VAIO Recovery Patcher (SVRP) - Batch v1.2
ECHO 2022 - Vir0z4 Network IT
ECHO.
ECHO Please read the documentation available on the GitHub before using SVRP! 
ECHO.
ECHO Make sure the folder with patchable files is writable, path contains no spaces, and contains only the .sny or .mod files you want to patch!
ECHO.

ECHO Select file extention
ECHO 1. .sny (Windows installation) (convertion to WIM)
ECHO 2. .mod (applications) (extracts to folder)
ECHO.
ECHO 3. Exit
ECHO.
SET /P M=Type 1, 2 or 3 and press ENTER: 
IF %M%==1 GOTO SNY
IF %M%==2 GOTO MOD
IF %M%==3 EXIT /B
IF %INPUT%==false EXIT /B

:SNY
CLS
SET /p "inputfolder=Copy and paste path to folder with patchable files: "
ECHO.
SET /p "f2=Enter name of first .sny file (usually has the shortest name) (example: sony.sny): "

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT %cd%\patchmod.exe %inputfolder%\%f2%
ECHO.
ECHO Process 1 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO If you already ran this process on this file and it was successful, it will always show an error when ran again, however please continue.
ECHO.
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
ECHO Please follow the documentation available on the SVRP GitHub to know how to install Windows from this WIM.
ECHO.

PAUSE
GOTO MENU

:MOD
CLS
SET /p "inputfoldermod=Copy and paste path to folder with patchable files: "
ECHO.
SET /p "m2=Enter name of .mod file to be extracted (example: MODJ-164418.mod): "

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT %cd%\patchmod.exe %inputfoldermod%\%m2%
ECHO.
ECHO Process 1 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO If you already ran this process on this file and it was successful, it will always show an error when ran again, however please continue.
ECHO.
PAUSE

CLS
ECHO Process 2 started...
ECHO.
START /B /WAIT cmd /c "mkdir %inputfoldermod%\extract"
START /B /WAIT cmd /c "%cd%\wimlib-imagex\wimlib-imagex.exe extract %inputfoldermod%\%m2% 1 --dest-dir=%inputfoldermod%\extract\%m2%"
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO.
ECHO The extracted .mod should now be in the folder "extract" in the folder with patchable files.
ECHO.

PAUSE
GOTO MENU