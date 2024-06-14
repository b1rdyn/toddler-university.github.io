from flask import Blueprint, render_template

varipeli_bp = Blueprint('varipeli', __name__, template_folder='templates')

@varipeli_bp.route('/varipeli')
def varipeli():
    return render_template('varipeli.html')