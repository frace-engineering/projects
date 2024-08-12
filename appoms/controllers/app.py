from flask import Blueprint, render_template


appomsbp = Blueprint('appomsbp', __name__)

@appomsbp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@appomsbp.route('/appoms/about', methods=['GET'])
def about():
    return render_template('about_us.html')

@appomsbp.route('/appoms/contact', methods=['GET'])
def contact():
    return render_template('contact_us.html')
