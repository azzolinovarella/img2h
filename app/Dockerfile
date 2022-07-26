FROM conda/miniconda3:latest

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./assets ./assets
COPY ./app.py ./environment.yml ./

# Gerando o env
RUN conda env create -f environment.yml --name app-env
### Faz com que os comandos RUN executem com o env ativo por padrão
SHELL ["conda", "run", "-n", "app-env", "/bin/bash", "-c"]

# Para rodar a aplicação
ENTRYPOINT ["streamlit", "run", "--browser.serverAddress", "app-env", "--browser.serverPort", "${PORT}", "--server.port ${PORT}", "--theme.base", "dark app.py"]