from flask import Blueprint, redirect, url_for,render_template,request
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        return render_template("sign_up.html", user=current_user)
    
    return render_template("home.html", user=current_user)
    
    #if current_user.is_authenticated:
    #    return redirect(url_for('links.dashboard'))    
    #return redirect(url_for('auth.login'))
