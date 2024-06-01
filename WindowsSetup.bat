@echo off
echo Installing packages
pip install -r requirements.txt
cd py
echo Building pointman
python setup.py build_ext --inplace