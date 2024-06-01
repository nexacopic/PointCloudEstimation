@echo off
cd py
del pointman.c
del pointman.html
del pointman.cp312-win_amd64.pyd
rd /s /q build
rd /s /q __pycache__