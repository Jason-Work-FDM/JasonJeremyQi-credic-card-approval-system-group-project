from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

import os


links = Blueprint('links', __name__)

@links.route('/user-dashboard', methods=['GET', 'POST'])
def user_dashboard():
    return render_template("User_dashboard.html", user=current_user)

@links.route('/user-info', methods=['GET', 'POST'])
def user_info():
    return render_template("User_info.html", user=current_user)

@links.route('/success', methods=['POST'])  
def success():  
    if request.method == 'POST': 
        f = request.files['file']
        upload_dir = './user_uploads/'
        user_path = os.path.join(upload_dir, str(current_user.id))
        if not os.path.isdir(user_path):
            os.mkdir(user_path)

        f.save(f"{user_path}/{f.filename}")

@links.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("User_dashboard.html", user=current_user)

@links.route('/apply', methods=['GET', 'POST'])
def apply():
    return render_template("apply.html", user=current_user)

@links.route('/spending_habits', methods=['GET', 'POST'])
def spending_habits():
    return render_template("spending_habits.html", user=current_user)
    
@links.route('/documents', methods=['GET', 'POST'])
def documents():
    return render_template("documents.html", user=current_user)