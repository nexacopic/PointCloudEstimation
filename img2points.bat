@echo off
IF [%1] == [] GOTO IncorrectUsage
IF [%2] == [] GOTO IncorrectUsage
python py/img2points.py %* %cd%
exit

:IncorrectUsage
echo img2points.bat [image path] [output model] [depth bias]
echo options:
exit
