#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate api-env
python api.py