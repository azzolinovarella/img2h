FROM conda/miniconda3:latest

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
SHELL ["conda", "run", "-n", "api-env", "/bin/bash", "-c"]
RUN pip install git+https://github.com/azzolinovarella/gameduino.git#subdirectory=src

# Para rodar a aplicação
ENTRYPOINT ["python", "api.py"]