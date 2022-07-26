#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate app-env
et -a && source .env && set +a  # Necessário para o heroku
# streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku
streamlit run --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku 