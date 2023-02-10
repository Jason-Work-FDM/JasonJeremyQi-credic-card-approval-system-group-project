from flask import Blueprint, current_app, flash, render_template, request, redirect, send_from_directory, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

import humanize

import time
import os

documents = Blueprint('documents', __name__)

@documents.route('/documents', methods=['GET', 'POST'])
def index():
    files = []
    user_path = f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}"
    if os.path.isdir(user_path):
        files = [f for f in os.listdir(user_path)]
    file_dict_list = []
    if files:
        for f in files:
            file_full_path = os.path.join(os.getcwd(), user_path, f)
            file_dict_list.append(
                {
                    'filename': f,
                    'upload_date':time.strftime('%d-%m-%Y', time.localtime(os.path.getmtime(file_full_path))),
                    'filesize':  humanize.naturalsize(os.stat(file_full_path).st_size)
                }
            )
    return render_template('documents.html', user=current_user, files=file_dict_list)

@documents.route('/uploads/<path:filename>', methods=['GET'])
def serve_file(filename):
    file_path = os.path.join(os.getcwd(), f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}")
    return send_from_directory(file_path, filename)

@documents.route('/delete/<path:filename>', methods=['DELETE', 'POST'])
def delete(filename):
    # Delete the file from the uploads folder
    file_path = os.path.join(os.getcwd(), f"{current_app.config['UPLOAD_FOLDER']}/{current_user.id}")
    os.remove(os.path.join(file_path, filename))
    flash(f"\"{filename}\" successfully deleted!")
    return redirect(url_for('documents.index'))
