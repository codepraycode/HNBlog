@echo off
:: This script is intended to install a python package and update requirements.txt
:: package name must be passed as first argument

echo installing %1...

pip install %1

if %ERRORLEVEL% EQU 0 echo Updateing requirements.txt && echo %1 >> requirements.txt