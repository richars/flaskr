@echo off
cd /d %~dp0
echo %cd%

set FLASK_APP=flaskr.py
venv\scripts\python -m flask run

exit