@ECHO off
:: This script is intended to install a python package and update requirements.txt
:: package name must be passed as first argument

ECHO installing %*...
pip install %*

IF  %ERRORLEVEL% EQU 1 GOTO ERROR
ECHO Updateing requirements.txt...

FOR %%e IN (%*) DO (
    ECHO %%e >> requirements.txt
)
ECHO Added package(s)
GOTO EOF

:ERROR
ECHO Could not add package(s)
::CMD /k
EXIT /b 1

:EOF