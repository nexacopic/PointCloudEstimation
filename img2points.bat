@echo off
IF [%1] == [] GOTO IncorrectUsage
python py/img2points.py %* %cd%
exit

:IncorrectUsage
echo img2points.bat [image path] [options]
echo options:
exit
