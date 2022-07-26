#!/bin/bash

streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku 