#!/bin/bash

python -m build
python -m pip install --force-reinstall ./dist/ft_package-0.0.1.tar.gz
python script.py
pip show -v ft_package
