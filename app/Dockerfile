FROM conda/miniconda3:latest

ARG APP_ENV=app-env  

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment.yml ./run.sh ./

# Gerando o env
RUN conda env create -f environment.yml --name ${APP_ENV}

# Para rodar a aplicação
ENTRYPOINT ["bash", "run.sh"]
