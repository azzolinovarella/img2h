FROM conda/miniconda3:latest

SHELL ["/bin/bash", "-c"]

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment.yml ./

# Gerando o env
RUN conda env create -f environment.yml --name app-env

# Para rodar a aplicação
CMD ["conda", "activate", "app-env", "&&", "streamlit", "run", "--browser.serverAddress", "app-env", "--browser.serverPort", "${PORT}", "--server.port ${PORT}", "--theme.base", "dark app.py"]