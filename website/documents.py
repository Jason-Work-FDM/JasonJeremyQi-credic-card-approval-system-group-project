from flask import Blueprint, current_app, flash, render_template, request, redirect, send_from_directory, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

import os


documents = Blueprint('documents', __name__)

@documents.route('/documents', methods=['GET', 'POST'])
def index():
    # Get list of all files in the uploads folder
    if os.path.isdir(current_app.config['UPLOAD_FOLDER']):
        files = [f for f in os.listdir(f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}") if os.path.isfile(os.path.join(f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}", f))]
    
    return render_template('documents.html', user=current_user, files=files)

@documents.route('/uploads/<path:filename>', methods=['GET'])
def serve_file(filename):
    file_path = os.path.join(os.getcwd(), f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}")
    return send_from_directory(file_path, filename)

@documents.route('/delete/<path:filename>', methods=['DELETE', 'POST'])
def delete(filename):
    # Delete the file from the uploads folder
    file_path = os.path.join(os.getcwd(), f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}")
    os.remove(os.path.join(file_path, filename))
    return redirect(url_for('documents.index'))
