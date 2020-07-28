import os

from flask import Flask, render_template, request, redirect

from inference import get_prediction
from commons import format_class_name
from werkzeug.utils import secure_filename

app = Flask(__name__)

def get_file_path_and_save(request):
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    return file_path

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

from PIL import Image

@app.route('/predictResNet50', methods=['GET', 'POST'])
def predictResNet50():
    if request.method == 'POST':
        file_path = get_file_path_and_save(request)
        im = Image.open(file_path)
        pred_class, class_name = get_prediction(image_bytes=im)
        result = format_class_name(class_name)




        

        return result
    return None
#-------------------------



if __name__ == '__main__':
    # Serve the app with gevent
      app.run(debug=True, port=int(os.environ.get('PORT', 5000)))