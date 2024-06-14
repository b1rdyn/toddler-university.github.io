from flask import Blueprint, render_template

numeropeli_bp = Blueprint('numeropeli', __name__, template_folder='templates')

@numeropeli_bp.route('/numeropeli')
def numeropeli():
    return render_template('numeropeli.html')