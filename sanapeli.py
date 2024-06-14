from flask import Blueprint, render_template

sanapeli_bp = Blueprint('sanapeli', __name__, template_folder='templates')

@sanapeli_bp.route('/sanapeli')
def sanapeli():
    return render_template('sanapeli.html')