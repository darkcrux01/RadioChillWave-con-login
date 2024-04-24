from flask import request, render_template, redirect, url_for, Blueprint

test = Blueprint('test', __name__, template_folder='templates')


@test.route('/')
def index():
    return render_template('index.html')