from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


	   
@auth.route("/sign-in")
def login():
    return render_template("signin.html")
   
@auth.route("/sign-up", methods=['POST', 'GET'])
def register():
    return render_template("signup.html")

@auth.route("/sign-out")
def logout():
    return "sign-out"
   