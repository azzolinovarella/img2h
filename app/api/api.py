from flask import Flask
from flask_restful import Api
from resources.index import Index
from resources.generate_image import GenerateImage
from resources.generate_sprite import GenerateSprite
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(GenerateImage, '/generate_image')
api.add_resource(GenerateSprite, '/generate_sprite')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ['API_PORT'])  # host nao muda
