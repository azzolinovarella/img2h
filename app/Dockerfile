FROM conda/miniconda3:latest

ARG APP_ENV="app-env"  

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment.yml ./

# Gerando o env
RUN conda env create -f environment.yml --name ${APP_ENV}
### Faz com que os comandos RUN executem com o env ativo por padrão
SHELL ["conda", "run", "-n", "${APP_ENV}", "/bin/bash", "-c"]

# Para rodar a aplicação
ENTRYPOINT ["streamlit", "run", "--browser.serverAddress", "${APP_URL}", "--browser.serverPort", "${PORT}", "--server.port ${PORT}", "--theme.base", "dark app.py"]