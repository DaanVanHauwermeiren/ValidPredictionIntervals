#!/bin/bash

# create venv
python3.10 -m venv .venv --prompt venv-predintvals
# activate env (not needed if explictly using pip from the venv)
source .venv/bin/activate
# install pip setuptools and wheel and update to latest version
.venv/bin/pip install --upgrade pip setuptools wheel
# install package
.venv/bin/pip install -e .
# add requirements
.venv/bin/pip install -r requirements.txt