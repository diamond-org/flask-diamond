REM Flask-Diamond (c) Ian Dennis Miller
REM This is a Windows batch file for launching flask-diamond
REM The script assumes you are using a python virtualenv.

REM First, we'll echo the command for debugging purposes
echo %VIRTUAL_ENV%\scripts\python.exe %VIRTUAL_ENV%\scripts\flask-diamond %*

REM Finally, we will execute the command
%VIRTUAL_ENV%\scripts\python.exe %VIRTUAL_ENV%\scripts\flask-diamond %*
