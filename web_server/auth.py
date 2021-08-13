from flask import Blueprint, render_template, redirect, request, url_for
from web_server import mysql
import MySQLdb.cursors
auth = Blueprint("auth", __name__)



@auth.route("/sign-in", methods=['POST','GET'])
def login():
	return render_template("signin.html")
   
@auth.route("/sign-up", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_info (username, password) VALUES (%s, %s)', (username, password ))
        mysql.connection.commit()
        cursor.close()  
#       INSERT INTO table_name (column1, column2, column3, ...)
#       VALUES (value1, value2, value3, ...);
    return render_template("signup.html")

@auth.route("/sign-out")
def logout():
    return redirect(url_for("views.home"))
   