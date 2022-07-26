#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
set -a && source .env && set +a  # Necessário para o heroku
### API
cd /api
conda activate api-env
nohup python api.py > /dev/null 2> /dev/null &  # So funfa no heroku se for assim
conda deactivate  
### APP
cd /app
conda activate app-env
streamlit run --server.enableCORS false --server.enableXsrfProtection false --server.port ${PORT} --theme.base dark app.py