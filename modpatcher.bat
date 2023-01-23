@echo off
ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (.mod patcher)

CLS
ECHO Process 1 started...
ECHO.
START /B /WAIT attrib -r %1\*.mod /s
START /B /WAIT C:\SVRP\patchmod.exe %1\%3
ECHO.
ECHO Process 1 completed.
ECHO.
ECHO If you already ran this process on this file and it was successful, it will always show an error when ran again, however please continue.
ECHO Some .mod files will show "Invalid header bytes detected" in this process, please continue anyway.
ECHO.
PAUSE

CLS
ECHO Process 2 started...
ECHO.
START /B /WAIT cmd /c "C:\SVRP\wimlib-imagex\wimlib-imagex.exe extract %1\%3 1 --dest-dir=%2\%3"
ECHO.
ECHO Process 2 completed.
ECHO.
ECHO If an error happened during this process, please try again.
ECHO.
ECHO The extracted .mod should now be in the output folder.
ECHO.
PAUSE
EXIT