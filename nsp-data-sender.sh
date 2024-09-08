#!/bin/bash

python -m venv .nsp-data-sender
source .nsp/bin/activate
pip install -r $PWD/requirements.txt
python $PWD/src/application.py --configuration $1 --nsp-configuration $2
