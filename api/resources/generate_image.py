from flask_restful import Resource, request
from PIL import Image
import gameduino.prep as gdprep
import uuid
import os

class GenerateImage(Resource):
    def post(self):
        fid = uuid.uuid4()   # para ter ctz que eh unico
        fname, fext = fid, None  # atualizado se receber o arquivo esperado 

        try:
            file = request.files['file']
            fname, fext = file.filename.split('.')
            file.save('./tmp/{0}.{1}'.format(fid, fext))
            im = Image.open("./tmp/{0}.{1}".format(fid, fext))  # Python 2 eh assim; nao da para usar o with... com o Image 
            gdprep.bgencode(im, "./tmp/{0}".format(fname), True)  # por enquanto nao vamos permitir mudar o nome e compress
            with open("./tmp/{0}.h".format(fname), "rb") as file:
                data = file.read()  # melhor maneira? e se retornarmos o arquivo direto? 

        except Exception as e:  # generico
            try:  # Para remover o arquivo MESMO que tenha dado algum erro antes!
                os.remove('./tmp/{0}.{1}'.format(fid, fext))
                os.remove('./tmp/{0}.h'.format(fname)) 
            except: pass  # Se der um erro dentro do erro para apagar...
            
            return {"message": "Exception: {0}".format(e), 
                    "data": None}, 500

        os.remove('./tmp/{0}.{1}'.format(fid, fext))
        os.remove('./tmp/{0}.h'.format(fname)) 
            

        return {"message": "ok", 
                "data": data}, 200        
