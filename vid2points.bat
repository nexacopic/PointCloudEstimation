@echo off
echo vid2points is unfished, do not use!
IF [%1] == [] GOTO IncorrectUsage
python py/vid2points.py %* %cd%
exit

:IncorrectUsage
echo vid2points.bat [image path] [options]
echo options:
exit
