FROM conda/miniconda3:latest

# Pasta onde vai estar os arquivos 
RUN mkdir /app
WORKDIR /app
ADD ./tmp ./tmp
ADD ./assets ./assets
COPY app.py environment.yml run.sh ./

# Gerando o env
## Necessário para o pillow!
RUN apt update && apt install gcc libx11-dev -y
RUN conda env create -f environment.yml --name png2h-env
# Para corrigir o gameduino!! 
RUN sed -i "/import Image/c\from PIL import Image" /usr/local/envs/png2h-env/lib/python2.7/site-packages/gameduino/prep.py

# Para rodar a aplicação
ENTRYPOINT ["bash", "run.sh"]