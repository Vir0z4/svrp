@echo off
ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (SVRP)

:MENU
CLS
ECHO Sony VAIO Recovery Patcher (SVRP) - Batch v1.3
ECHO 2022 - Vir0z4 Network IT
ECHO.
ECHO Please read the documentation available on the GitHub before using SVRP! 
ECHO.
ECHO Make sure the folder with patchable files is writable, path contains no spaces, and contains only the .sny or .mod files you want to patch! Make sure file names also don't contain spaces!
ECHO.

ECHO Select file extention
ECHO 1. .sny (Windows installation) (convertion to WIM)
ECHO 2. .mod (applications) (extracts to folder)
ECHO 3. Custom extention (experimental) (only if you know what you are doing)
ECHO.
ECHO 4. Exit
ECHO.
SET "M="
SET /P M=Type 1, 2, 3 or 4 and press ENTER: 
IF "%M%"=="1" GOTO SNY
IF "%M%"=="2" GOTO MOD
IF "%M%"=="3" GOTO EX
IF "%M%"=="4" EXIT /B
ELSE
GOTO MENU

:SNY
CLS
SET "inputfolder="
SET "f2="
SET /p "inputfolder=Copy and paste path to folder with patchable files: "
IF "%inputfolder%"=="" GOTO SNY
ECHO.
SET /p "f2=Enter name of first .sny file (usually has the shortest name) (example: sony.sny): "
IF "%f2%"=="" GOTO SNY

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %inputfolder%\*.* /s
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
SET "inputfoldermod="
SET "m2="
SET /p "inputfoldermod=Copy and paste path to folder with patchable files: "
IF "%inputfoldermod%"=="" GOTO MOD
ECHO.
SET /p "m2=Enter name of .mod file to be extracted (example: MODJ-164418.mod): "
IF "%m2%"=="" GOTO MOD

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %inputfoldermod%\*.* /s
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
GOTO MENUMOD

:MENUMOD
CLS
ECHO 1. Would you like to extract another .mod? (same input directory)
ECHO 2. Return to menu
ECHO.
SET "Z="
SET /P Z=Type 1 or 2 and press ENTER: 
IF "%Z%"=="1" GOTO MODR
IF "%Z%"=="2" GOTO MENU
ELSE
GOTO MENUMOD

:MODR
CLS
SET "m2="
SET /p "m2=Enter name of .mod file to be extracted (example: MODJ-164418.mod): "
IF "%m2%"=="" GOTO MODR

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %inputfoldermod%\*.* /s
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
START /B /WAIT cmd /c "%cd%\wimlib-imagex\wimlib-imagex.exe extract %inputfoldermod%\%m2% 1 --dest-dir=%inputfoldermod%\extract\%m2%"
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO.
ECHO The extracted .mod should now be in the folder "extract" in the folder with patchable files.
ECHO.

PAUSE
GOTO MENUMOD

:EX
CLS
ECHO This is an experimental feature!
ECHO Please only use this if you know what you are doing!
ECHO.
PAUSE
GOTO EX2

:EX2
CLS
SET "inputfolderex="
SET "e2="
SET /p "inputfolderex=Copy and paste path to folder with files: "
IF "%inputfolderex%"=="" GOTO EX2
ECHO.
SET /p "e2=Enter name of first file (with extention) (usually has the shortest name) (example: sony.img): "
IF "%e2%"=="" GOTO EX2
ECHO.
SET /p "ee2=Enter extention with dot (example: .img): "
IF "%ee2%"=="" GOTO EX2

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %inputfolderex%\*.* /s
START /B /WAIT %cd%\patchmod.exe %inputfolderex%\%e2%
ECHO.
ECHO Process 1 completed.
ECHO.
PAUSE

CLS
ECHO Process 2 started...
ECHO.
START /B /WAIT cmd /c "%cd%\wimlib-imagex\wimlib-imagex.exe export %inputfolderex%\%e2% 1 %inputfolderex%\sony.wim "Sony" --ref="%inputfolderex%\*%ee2%""
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO Please check for a WIM in the input directory.
ECHO.

PAUSE
GOTO MENU