@echo off
ECHO OFF & COLOR 17
CLS & TITLE Sony VAIO Recovery Patcher (.mod automatic patcher)

ECHO Sony VAIO Recovery Patcher - Auto .mod patcher
ECHO.
ECHO WARNING:
ECHO Some .mod files will show "Invalid header bytes detected" in process 1, this is normal.
ECHO If you already ran process 1 on a .mod file and it was successful, it will always show an error when ran again, this is normal.
ECHO.
PAUSE

for %%f in (%1\*.mod) do (
  CLS
  ECHO Process 1 started...
  ECHO.
  START /B /WAIT attrib -r %1\*.mod /s
  START /B /WAIT C:\SVRP\patchmod.exe %1\%%f
  ECHO.
  ECHO Process 1 completed.
  ECHO.
  ECHO Process 2 started...
  ECHO.
  START /B /WAIT cmd /c "C:\SVRP\wimlib-imagex\wimlib-imagex.exe extract %%f 1 --dest-dir=%2\%%~nf"
  ECHO.
  ECHO Process 2 completed.
  ECHO.
  PAUSE
)

CLS
ECHO SVRP auto .mod patcher has completed.
ECHO.
ECHO The extracted .mod files should now be in the output folder.
ECHO.
ECHO If an error happened during the extraction of one .mod file, please use the manual patcher to extract that file.
PAUSE
EXIT