from flask import Flask, send_from_directory
from flask_restx import Api, Resource, fields
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Image API', description='An API to retrieve images by category')

# Definindo os modelos
image_model = api.model('Image', {
    'url': fields.String(description='Image URL')
})

images_model = api.model('Images', {
    'images': fields.List(fields.Nested(image_model), description='List of images')
})

# Diretório onde as imagens estão armazenadas
images_directory = './api/images'

# Função para listar as pastas (categorias) de imagens
def list_folders(directory):
    folders = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            folders.append(item)
    return folders

# Rota para listar imagens de uma categoria específica
@api.route('/images/<category>')
@api.doc(params={'category': 'Category of images'})
class Images(Resource):
    @api.marshal_with(images_model)
    @api.doc(description='Get a list of images for a specific category')
    def get(self, category):
        """
        Get a list of images for a specific category
        
        :param category: Category of images
        :return: List of images
        """
        category_directory = os.path.join(images_directory, category)
        if os.path.exists(category_directory):
            images = [{'url': f'/images/{category}/{image}'} for image in os.listdir(category_directory)]
            return {'images': images}
        else:
            api.abort(404, f'Category {category} not found')

# Rota para obter uma imagem específica
@api.route('/images/<category>/<path:image>')
@api.doc(params={'category': 'Category of the image', 'image': 'Image name'})
class Image(Resource):
    @api.doc(description='Get a specific image by category and image name')
    def get(self, category, image):
        """
        Get a specific image by category and image name
        
        :param category: Category of the image
        :param image: Image name
        :return: The requested image
        """
        image_path = os.path.join(images_directory, category, image)
        if os.path.exists(image_path):
            return send_from_directory(images_directory, f'{category}/{image}')
        else:
            api.abort(404, f'Image {image} not found')

# Loop para adicionar recursos para cada categoria de imagem
for folder in list_folders(images_directory):
    api.add_resource(Images, f'/images/{folder}')

if __name__ == '__main__':
    app.run(debug=True)
