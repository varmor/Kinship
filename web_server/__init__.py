from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
# from flask_login import LoignManager


def create_server():
	server = Flask(__name__)

	server.config['SECRET_KEY'] ="secretkey"
	@server.route("/")
	def index():
	    return render_template("index.html")
	   
	@server.route("/signin")
	def login():
	    return render_template("signin.html")
	   
	@server.route("/signup", methods=['POST', 'GET'])
	def register():
	    return render_template("signup.html")

	return server
	   