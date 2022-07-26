FROM conda/miniconda3:latest

ARG API_ENV=api-env

# Pasta onde vai estar os arquivos 
RUN mkdir /api
WORKDIR /api
### sepa desnecessario o tmp...
ADD ./tmp ./tmp
ADD ./resources ./resources 
COPY ./api.py ./environment.yml ./run.sh ./

# Gerando o env
## Necessário para o pillow!
RUN apt update && apt install gcc libx11-dev git -y
RUN conda env create -f environment.yml --name ${API_ENV}
RUN conda run -n ${API_ENV} pip install git+https://github.com/azzolinovarella/gameduino.git#subdirectory=src

RUN conda activate ${API_ENV}

# Para rodar a aplicação
ENTRYPOINT ["bash", "run.sh"]
