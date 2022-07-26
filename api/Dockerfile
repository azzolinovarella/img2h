FROM conda/miniconda3:latest

SHELL ["/bin/bash", "-c"]

# Pasta onde vai estar os arquivos 
RUN mkdir /api
WORKDIR /api
### sepa desnecessario o tmp...
ADD ./tmp ./tmp
ADD ./resources ./resources 
COPY ./api.py ./environment.yml ./

# Gerando o env
## Necessário para o pillow!
RUN apt update && apt install gcc libx11-dev git -y
RUN conda env create -f environment.yml --name api-env
### Faz com que os comandos RUN executem com o env ativo por padrão
RUN conda run -n api-env pip install git+https://github.com/azzolinovarella/gameduino.git#subdirectory=src

# Para rodar a aplicação
CMD ["conda", "activate", "api-env", "&&", "python", "api.py"]