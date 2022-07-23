#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda activate ${APP_ENV}

### Heroku
# streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${PORT} --server.port ${PORT} --theme.base dark app.py  # Heroku 
### Local
streamlit run --browser.serverAddress ${APP_URL} --browser.serverPort ${APP_PORT} --server.port ${APP_PORT} --theme.base dark app.py  # Local 