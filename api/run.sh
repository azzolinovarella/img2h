#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate api-env
set -a && source .env && set +a  # Necessário para o heroku
python api.py