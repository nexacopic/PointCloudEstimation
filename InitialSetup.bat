@echo off
cd %~dp0
echo #############################
echo ##   Installing packages   ##
echo #############################
pip install --user --upgrade --force-reinstall -r requirements.txt
cd py
echo ###########################
echo ##   Building pointman   ##
echo ###########################
python setup.py build_ext --inplace
echo ###################
echo ##   Finished!   ##
echo ###################
pause