from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sanapeli')
def sanapeli():
    return render_template('sanapeli.html')

@app.route('/numeropeli')
def numeropeli():
    return render_template('numeropeli.html')

@app.route('/kirjainpeli')
def kirjainpeli():
    return render_template('kirjainpeli.html')

if __name__ == '__main__':
    app.run(debug=True)
