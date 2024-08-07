from flask import Blueprint, render_template, request, url_for, redirect


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def index():
    return 'Hello flask-python'

@user_bp.route('/home')
def home():
    return 'Home'
