from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required
from flask_login import login_required, current_user


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/professionals')

def professionals():
    return render_template('professionals.html')

@main.route('/architect')
@login_required
def architect():
    return render_template('architects.html')

@main.route('/engineers')
@login_required
def engineers():
    return render_template('engineers.html')

@main.route('/constructors')
@login_required
def constructors():
    return render_template('constructors.html')