from flask import Blueprint, render_template
from flask import Flask, render_template, url_for
import random
import os

sanapeli_bp = Blueprint('sanapeli', __name__, template_folder='templates')

app = Flask(__name__)

PICTURE_FILE = 'static/sanapeli/'

@sanapeli_bp.route('/sanapeli')
def sanapeli():
    picture_files = os.listdir(PICTURE_FILE)
    random_image = random.choice(picture_files)
    word = os.path.splitext(random_image)[0]
    image_route = url_for('static', filename=f'sanapeli/{random_image}')
    return render_template('sanapeli.html', kuva_url=image_route, sana=word)


@sanapeli_bp.route('/sanapeli')
def sanapeli_next():
    return sanapeli()


if __name__ == '__main__':
    app.run(debug=True)