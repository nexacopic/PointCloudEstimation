@echo off
IF [%1] == [] GOTO IncorrectUsage
IF [%2] == [] GOTO IncorrectUsage
IF [%3] == [] GOTO IncorrectUsage
IF [%4] == [] GOTO IncorrectUsage
python py/img2points.py %* %cd%
EXIT /B

:IncorrectUsage
echo img2points.bat [image path] [output model] [depth bias] [gpulevel]
echo options:
EXIT /B
