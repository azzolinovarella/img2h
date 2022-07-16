from shutil import ExecError
import streamlit as st
import datetime as dt
import gameduino.prep as gdprep
from PIL import Image
import base64
import os
import sys

# Se não buga os acentos
reload(sys) 
sys.setdefaultencoding('utf8')

st.write("# PNG2H")
# st.image("./assets/logo.png")
st.write("Partindo de imagens em formato PNG, gera os arquivos de inclusão de gráficos embarcados".encode('utf8'))

uploaded_file = st.file_uploader("Insira o arquivo png", type="png")

if uploaded_file is not None:
    date = str(dt.datetime.now())  # Apenas para ter certeza de que não vamos ter 2 pessoas ao mesmo tempo subindo arquivo

    exported_file_path = "./tmp/converted_file-" + date + ".h"
    image_file_path = './tmp/base_file-'+ date + '.png'

    try:
        with open(image_file_path, 'wb') as file:
            file.write(uploaded_file.getvalue())

        (dpic, dchr, dpal) = gdprep.encode(Image.open(image_file_path))  # Aparentemente não dá para fechar

        with open(exported_file_path, "w") as hdr:
            gdprep.dump(hdr, "titlescreen_pic", dpic)
            gdprep.dump(hdr, "titlescreen_chr", dchr)
            gdprep.dump(hdr, "titlescreen_pal", dpal)

        # Nessa versão do streamlit só
        with open(exported_file_path, 'rb') as file:
            # Tem que ser assim porque essa versão do Streamlit não tem o "download_button"
            st.write('<div style="text-align:center"><a href="data:file/h;base64,' + base64.b64encode(file.read()).decode() + '" download="converted_file.h"><button>Baixar arquivo convertido</button></a></div>', unsafe_allow_html=True)

    except Exception as e:  # Genérico
        st.warning("Não foi possível gerar seu arquivo. Verifique se o arquivo está no formato correto e tente novamente.")

    # No final, remove os arquivos temporários (mesmo que tenha dado erro!):
    try:
        os.remove(image_file_path)
        os.remove(exported_file_path)
    except: 
        pass 