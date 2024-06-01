@echo off
echo #############################
echo ##   Installing packages   ##
echo #############################
pip install -r requirements.txt
cd py
echo ###########################
echo ##   Building pointman   ##
echo ###########################
python setup.py build_ext --inplace
cls
echo ###################
echo ##   Finished!   ##
echo ###################
pause