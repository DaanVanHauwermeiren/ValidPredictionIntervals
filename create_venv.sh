#!/bin/bash

# create venv
python3.10 -m venv .venv --prompt venv-predintvals
# activate env (not needed if explictly using pip from the venv)
source .venv/bin/activate
# install pip setuptools and wheel and update to latest version
.venv/bin/pip install --upgrade pip setuptools wheel
# install package
.venv/bin/pip install -e .
# add additional requirements for development
.venv/bin/pip install --upgrade -r requirements-dev.txt

# setup pre-commit
pre-commit uninstall
pre-commit install
pre-commit install --install-hooks
