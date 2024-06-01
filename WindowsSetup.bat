@echo off
echo Installing packages
pip install -r requirements.txt
echo Cleaning up any loose files
./Clean.bat

echo Building pointman
python setup.py build_ext --inplace