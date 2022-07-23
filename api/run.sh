#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate ${API_ENV}
python api.py