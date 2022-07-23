import streamlit as st
import requests
import os
import logging
import requests
import time


def render_generate_image():
    st.write("Insira sua imagem pelo uploader abaixo (dê preferencia por utilizar PNG)")
    st.write("**ATENÇÃO, O ARQUIVO DEVE TER RESOLUÇÃO DE 416x320 PIXELS E NÃO POSSUIR MAIS DE 256 CORES.**")
    file = st.file_uploader("Insira a imagem de fundo", type=['png', 'bmp', 'jpg', 'jpeg'])
    try:
        if file is not None:
            with st.spinner("Gerando imagem..."):
                time.sleep(1)  # Para evitar sobrecarga
                res = requests.post(
                    url=f"http://{os.environ['API_URL']}:{os.environ['API_PORT']}/generate_image", 
                    files=[('file',('image.png', file.getvalue(), file.type))],
                    headers={}, 
                    data={})

                res_json = res.json()
                if res.status_code == 200:
                    st.download_button("Baixar imagem", data=res_json['data'], file_name=file.name.split('.')[0] + '.h')               
                else:
                    st.warning("Houve algum problema ao gerar sua imagem. Atente-se as exigências e submeta novamente")
                
                logging.info(f"({res.status_code}) {res_json['message']}")

    except Exception as e:
        st.warning("Houve algum problema ao realizar a conversão. Se o erro persistir, entre em contato.")
        st.write('### <center><a href="mailto:f.azzolinovarella@gmail.com">Enviar um e-mail para f.azzolinovarella@gmail.com</a></center>', unsafe_allow_html=True)
        logging.warning(f"(500) Exception - {e}")


def render_generate_sprite():
    st.write("Insira seu sprite pelo uploader abaixo (deve estar em formato PNG)")
    file = st.file_uploader("Insira o sprite", type=['png'])
    try:
        if file is not None:
            col1, col2 = st.columns([1, 1])
            width = col1.number_input("Largura", min_value=0, step=1)
            height = col2.number_input("Altura", min_value=0, step=1)

            if width != 0 and height != 0:
                with st.spinner("Gerando sprite..."):
                    time.sleep(1)  # Para evitar sobrecarga
                    res = requests.post(
                        url=f"http://{os.environ['API_URL']}:{os.environ['API_PORT']}/generate_sprite",
                        files={'file': ('image.png', file.getvalue(), file.type),
                               'width': (None, width, 'text'),
                               'height': (None, height, 'text')},
                        headers={}, 
                        data={})

                    res_json = res.json()
                    if res.status_code == 200:
                        st.download_button("Baixar sprite", data=res_json['data'], file_name=file.name.split('.')[0] + '.h')               
                    else:
                        st.warning("Houve algum problema ao gerar seu sprite. Atente-se as exigências e submeta novamente")
                    
                    logging.info(f"({res.status_code}) {res_json['message']}")

    except Exception as e:
        st.warning("Houve algum problema ao realizar a conversão. Se o erro persistir, entre em contato.")
        st.write('### <center><a href="mailto:f.azzolinovarella@gmail.com">Enviar um e-mail para f.azzolinovarella@gmail.com</a></center>', unsafe_allow_html=True)
        logging.warning(f"(500) Exception - {e}")


def main():
    st.write("# PNG2H")
    
    opt = st.selectbox("Selecione o tipo de geração", options=['...', 'Background', 'Sprite'], index=0)
    
    if opt == 'Background':
        render_generate_image()
    
    elif opt == 'Sprite':
        render_generate_sprite()


if __name__ == "__main__":
    global session
    session = requests.Session()   
    main()