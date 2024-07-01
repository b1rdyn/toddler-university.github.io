from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
login_bp = Blueprint('login', __name__, template_folder='templates')
 
app = Flask(__name__)
 
 
app.secret_key = 'SECRET_KEY'

app.config['MYSQL_DB'] = 'login1'
 
mysql = MySQL(app)
 
@login_bp.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Sisäänkirjautuminen onnistui!'
            return render_template('pelit.html', msg = msg)
        else:
            msg = 'Väärä käyttäjätunnus tai salasana!'
    return render_template('pelit.html', msg = msg)
 
@login_bp.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
 
@login_bp.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Käyttäjä on jo olemassa'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Käyttäjänimi voi sisältää vain kirjaimia ja numeroita!'
        elif not username or not password:
            msg = 'Täytä vaadittavat kohdat'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, ))
            mysql.connection.commit()
            msg = 'Käyttäjätunnus luotu'
    elif request.method == 'POST':
        msg = 'Täytä vaadittavat kohdat'
    return render_template('register.html', msg = msg)

if __name__ == '__main__':
    app.register_blueprint(login_bp)
    app.run(debug=True)
