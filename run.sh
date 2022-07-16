#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda run -n png2h-env streamlit run --browser.serverAddress 'https://png2h.herokuapp.com/' --browser.serverPort $PORT --server.port $PORT app.py # Para rodar no heroku! 