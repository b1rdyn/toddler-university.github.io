from flask import Flask, render_template
from sanapeli import sanapeli_bp
from numeropeli import numeropeli_bp
from kirjainpeli import kirjainpeli_bp
from varipeli import varipeli_bp

app = Flask(__name__)

app.register_blueprint(sanapeli_bp)
app.register_blueprint(numeropeli_bp)
app.register_blueprint(kirjainpeli_bp)
app.register_blueprint(varipeli_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)