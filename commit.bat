@echo off

:: This programs handles commiting
:: receives a message parameter

:: Stash all as usual
git add .

:: commit with given message
git commit -m %1

:: Push commit
git push origin
