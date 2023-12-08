#!/bin/bash

echo "Program Starts"

echo "Compile python script"
python3 -m py_compile test.py 

echo "Run python script"
python3 test.py

echo "Remove compiled file"
rm -f __pycache__/main.*
