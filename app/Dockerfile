FROM conda/miniconda3:latest

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment.yml ./run.sh ./.env ./

# Gerando o env
RUN conda env create -f environment.yml --name app-env

# Para rodar a aplicação
CMD ["bash", "run.sh"]