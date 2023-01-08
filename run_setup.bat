@ECHO off
:: This script is intended to setup project for development
:: it runs pip installation and npm installation
ECHO Running HNBlog app development setup.
ECHO setting up backend...
pip install -r requirements.txt

IF  %ERRORLEVEL% EQU 1 GOTO ERROR
ECHO setting up frontend...
npm install

IF  %ERRORLEVEL% EQU 1 GOTO ERROR
ECHO App is now ready for development, frontend runs at port 5713 and backend runs at port 5714
GOTO EOF

:ERROR
ECHO Could not setup project, try again or check contribution instruction at https://github.com/codepraycode/HNBlog
::CMD /k
EXIT /b 1

:EOF