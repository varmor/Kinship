from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_server():
	server = Flask(__name__)
	server.config['SECRET_KEY'] ="secretkey"

	from .views import views
	from .auth import auth

	server.register_blueprint(views, url_prefix="/")
	server.register_blueprint(auth, url_prefix="/")
	return server
	   