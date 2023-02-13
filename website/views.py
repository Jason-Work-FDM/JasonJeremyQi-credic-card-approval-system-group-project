from flask import Blueprint, redirect, url_for,render_template
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)


    
    

