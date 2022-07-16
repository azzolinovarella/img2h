#!/bin/bash

conda init > /dev/null 2> /dev/null && source ~/.bashrc
conda run -n png2h-env streamlit run app.py --server.port 8080 