from flask import request, render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, current_user, login_required

from bprintapp.app import db
from bprintapp.app import bcrypt

from bprintapp.blueprints.users.models import User

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/', methods=['GET', 'POST'])
def index():
    return render_template('users/index.html', current_user=current_user)


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'GET':
        return render_template('users/signup.html')
    elif request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.index'))



@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.username == username).first()

        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('users.index'))

        else:
            return "Fail"



@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))   

@users.route('/secret')
@login_required
def secret():
    if current_user.role == 'admin':
        return 'Secret message'
    else:
        return "No permission"
