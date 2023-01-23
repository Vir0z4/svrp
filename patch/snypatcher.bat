@echo off
ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (.sny patcher)

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %1\*.sny /s
START /B /WAIT C:\SVRP\patchmod.exe %1\%3

ECHO.
ECHO Process 1 completed.
ECHO.
ECHO If an error happened during this process, please try again.
ECHO If you already ran this process on this file and it was successful, it will always show an error when ran again, this is normal.
ECHO.
PAUSE

CLS
ECHO Process 2 started...
ECHO.
START /B /WAIT cmd /c "C:\SVRP\wimlib-imagex\wimlib-imagex.exe export %1\%3 1 %2\sony.wim "Sony" --ref="%1\*.sny""
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during this process, please try again.
ECHO.
ECHO The WIM file should now be in the output folder.
ECHO Please follow the documentation available on the SVRP GitHub to know how to install Windows from this WIM.
ECHO.
PAUSE
EXIT