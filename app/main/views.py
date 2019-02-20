from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required
from flask_login import login_required, current_user


@main.route('/')
def index():
    return render_template('index.html')