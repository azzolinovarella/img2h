FROM conda/miniconda3:latest

ARG APP_ENV=png2h_app-env  

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./app/assets ./assets
COPY ./app/app.py ./app/environment.yml ./app/run.sh ./

# Gerando o env
RUN conda env create -f environment.yml --name ${APP_ENV}

# Para rodar a aplicação
ENTRYPOINT ["bash", "run.sh"]