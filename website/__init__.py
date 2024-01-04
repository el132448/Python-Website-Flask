from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # __name__:name of the file ran
    app.config['SECRET_KEY'] = 'asdsadsadsaa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # create database
    from . import models
    with app.app_context():
        db.create_all()

    # load user for flask login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

# Outdated!
# def create_database(app):
#     # check if the database exist, not to override the exist database
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Create Database!')