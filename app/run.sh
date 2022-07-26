#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate app-env

streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku 