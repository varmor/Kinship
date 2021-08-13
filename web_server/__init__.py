from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from os import path
from flask_login import LoginManager


server = Flask(__name__)
server.config['SECRET_KEY'] ="secretkey"
# SQL alchemy database 
# server.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/user'
server.config['MYSQL_HOST'] = 'localhost'
server.config['MYSQL_USER'] = 'root'
server.config['MYSQL_PASSWORD'] = ''
server.config['MYSQL_DB'] = 'user'
server.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# db = SQLAlchemy(app)
# class for model 
# class UserInfo(db.Model):
 #    id = db.Column(db.Integer, primary_key=True)
 #    username = db.Column(db.String(80), unique=True, nullable=False)
 #    email = db.Column(db.String(120), unique=True, nullable=False)


mysql = MySQL(server)

from .views import views
from .auth import auth

server.register_blueprint(views, url_prefix="/")
server.register_blueprint(auth, url_prefix="/")

