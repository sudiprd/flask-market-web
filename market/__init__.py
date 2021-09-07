from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']= '754bc527226a999f68a22f28'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category= "info"
from market import routes

#dynamic route
# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>Hello World from About Page {username} </h1>'