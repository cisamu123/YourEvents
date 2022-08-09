echo off

nul > events.txt

pip install datetime
pip install pyinstaller

pyinstaller -F -w -i icon.ico Event.py


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null