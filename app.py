from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sanapeli')
def sanapeli():
    return render_template('sanapeli.html')

@app.route('/numeropeli')
def numeropeli():
    return render_template('numeropeli.html')

@app.route('/kirjainpeli', methods=['GET', 'POST'])
def kirjainpeli():
    message = ''
    if request.method == 'GET':
        letter_to_display = random.choice(string.ascii_uppercase)
    else:
        user_input = request.form['input_letter'].upper()
        correct = (user_input == request.form['hidden_letter'])
        if correct:
            message = 'Oikein!'
            letter_to_display = random.choice(string.ascii_uppercase)
        else:
            message = 'Yritä uudelleen'
            letter_to_display = request.form['hidden_letter']
    return render_template('kirjainpeli.html', letter=letter_to_display, message=message)

@app.route('/varipeli')
def varipeli():
    return render_template('varipeli.html')

if __name__ == '__main__':
    app.run(debug=True)
