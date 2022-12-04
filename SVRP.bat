::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFClkRQiLPVeeCaIS5Of66/m7sVsPRK89eZvY0oidNvIDp0flYZUl6klsqvtCCQNdHg==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (SVRP)

ECHO Sony VAIO Recovery Patcher (SVRP) - Batch v1.1
ECHO 2022 - Vir0z4 Network IT
ECHO.
ECHO This tool supports .sny and .mod files ONLY (for now)!
ECHO.
ECHO Make sure the folder with patchable files is writable, path contains NO spaces, and contains only the .sny or .mod files you want to patch!
ECHO.

:MENU
ECHO Select file extention
ECHO 1. .sny (Windows installation) (convertion to WIM)
ECHO 2. .mod (applications) (extracts to folder) (not needed for Windows install)
ECHO.
SET /P M=Type 1 or 2 and press ENTER: 
IF %M%==1 GOTO SNY
IF %M%==2 GOTO MOD
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
ECHO For more information on how to install this WIM file, please follow the documentation on the SVRP GitHub repository.
ECHO.

PAUSE
EXIT /B

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
START /B /WAIT cmd /c "%cd%\wimlib-imagex\wimlib-imagex.exe extract %inputfoldermod%\%m2% 1 --dest-dir=%inputfoldermod%\extract"
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during the process, please try again.
ECHO.
ECHO The extracted .mod should now be in the "extract" folder in the input folder (folder with patchable files).
ECHO.

PAUSE
EXIT /B