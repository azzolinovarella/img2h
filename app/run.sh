#!/bin/bash

conda activate ${APP_ENV}
streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku 