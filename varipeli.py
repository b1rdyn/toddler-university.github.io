from flask import Blueprint, render_template, Flask, url_for, request, redirect
import random
import os

varipeli_bp = Blueprint('varipeli', __name__, template_folder='templates')

app = Flask(__name__)

PICTURE_FILE = 'static/varipeli/'

def get_random_images():
    picture_files = [file for file in os.listdir(PICTURE_FILE) if os.path.isfile(os.path.join(PICTURE_FILE, file))]
    return random.sample(picture_files, 3)

@varipeli_bp.route('/varipeli')
def varipeli():
    random_images = get_random_images()
    right_image = random.choice(random_images)
    right_image_name = right_image.split('.')[0]
    return render_template('varipeli.html', kuvat=random_images, correct_word=right_image_name)

@varipeli_bp.route('/varipeli', methods=['POST'])
def varipeli_validate():
    selected_word = request.form.get('selected_word')
    correct_word = request.form.get('correct_word')
    random_images = [request.form['kuva_' + str(i)] for i in range(3)]

    if selected_word == correct_word:
        return redirect(url_for('varipeli.varipeli'))
    else:
        return render_template('varipeli.html', message="Yritä uudelleen", 
                               kuvat=random_images, correct_word=correct_word)

if __name__ == '__main__':
    app.run(debug=True)
