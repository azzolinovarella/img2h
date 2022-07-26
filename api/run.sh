#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate api-env
source ./.env  # Necessário para o heroku
python api.py