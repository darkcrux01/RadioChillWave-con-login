from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_inner_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'
    app.secret_key ='SOME KEY'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)


    from bprintapp.blueprints.users.models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)

    @login_manager.unauthorized_handler
    def unauthorize_callback():
        return redirect(url_for('index'))
    
    

    global bcrypt
    bcrypt = Bcrypt(app)
    #print(bcrypt)

    #import and register blueprints
    from bprintapp.blueprints.test.routes import test
    from bprintapp.blueprints.users.routes import users

    #from blueprintapp.blueprints.todos.routes import todos
    #from blueprintapp.blueprints.people.routes import people

    app.register_blueprint(test, url_prefix='/')
    app.register_blueprint(users, url_prefix='/users')
    #app.register_blueprint(todos, url_prefix='/todos')
    #app.register_blueprint(people, url_prefix='/people')

    migrate = Migrate(app, db)

    return app

def create_app():
    app = create_inner_app()
    bcrypt = Bcrypt(app)
    return app