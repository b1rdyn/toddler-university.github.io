from flask import Blueprint, render_template, Flask, url_for, request, redirect
import random
import os

numeropeli_bp = Blueprint('numeropeli', __name__, template_folder='templates')

app = Flask(__name__)

PICTURE_FILE = 'static/numeropeli/'

def get_random_words(count, correct_word):
    picture_files = os.listdir(PICTURE_FILE)
    words = [os.path.splitext(file)[0] for file in picture_files if os.path.splitext(file)[0] != correct_word]
    random_words = random.sample(words, count - 1)
    random_words.append(correct_word)
    random.shuffle(random_words)
    return random_words

@numeropeli_bp.route('/numeropeli')
def numeropeli():
    picture_files = os.listdir(PICTURE_FILE)
    random_image = random.choice(picture_files)
    word = os.path.splitext(random_image)[0]
    image_route = url_for('static', filename=f'numeropeli/{random_image}')
    words = get_random_words(3, word)
    return render_template('numeropeli.html', kuva_url=image_route, sana=word, words=words)

@numeropeli_bp.route('/numeropeli', methods=['POST'])
def numeropeli_validate():
    selected_word = request.form.get('selected_word')
    correct_word = request.form.get('correct_word')
    if selected_word == correct_word:
        return redirect(url_for('numeropeli.numeropeli'))
    else:
        return render_template('numeropeli.html', message="Yritä uudelleen", words=get_random_words(3, correct_word), kuva_url=url_for('static', filename=f'numeropeli/{correct_word}.webp'), sana=correct_word)

if __name__ == '__main__':
    app.register_blueprint(numeropeli_bp, url_prefix='/numeropeli')
    app.run(debug=True)
