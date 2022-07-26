#!/bin/bash

# conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda init bash || source ~/.bashrc
conda activate ${API_ENV}
python api.py