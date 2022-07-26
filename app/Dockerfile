FROM conda/miniconda3:latest

##### APP
# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment-app.yml ./run.sh ./.env ./
# Gerando o env
RUN conda env create -f environment-app.yml --name app-env

##### API
# Pasta onde vai estar os arquivos 
RUN mkdir /api
WORKDIR /api
### sepa desnecessario o tmp...
ADD ./api/tmp ./tmp
ADD ./api/resources ./resources 
COPY ./api/api.py ./api/environment-api.yml ./
# Gerando o env
## Necessário para o pillow!
RUN apt update && apt install gcc libx11-dev git -y
RUN conda env create -f environment-api.yml --name api-env
RUN conda run -n api-env pip install git+https://github.com/azzolinovarella/gameduino.git#subdirectory=src

# Para rodar a aplicação
WORKDIR /app
CMD ["bash", "run.sh"]