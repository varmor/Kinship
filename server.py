from flask import Flask, render_template, url_for

server = Flask(__name__)

@server.route("/")
def index():
    return render_template("index.html")
   
@server.route("/signin")
def login():
    return render_template("signin.html")
   
@server.route("/signup")
def register():
    return render_template("signup.html")
   
if __name__ == '__main__':
    server.run(debug=True)