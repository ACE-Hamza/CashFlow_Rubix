from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlite3
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("spend.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/")
def sign():
	return redirect(url_for("signup"))

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/signup.html", methods=["POST", "GET"])
def signup():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        session.permanent = True
        uname = request.form["uname"]
        email = request.form["email"]
        name = request.form["name"]
        pswd = request.form["pswd"]
        # session["user"] = uname
        sql = """INSERT INTO users (email, uname, name, pswd)
                 VALUES (?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (email, uname, name, pswd))
        conn.commit()
        return redirect(url_for("homepage"))
    # else:
    #     if "user" in session:
    #         return redirect(url_for("user"))
    return render_template("signup.html")
    
@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")
if __name__ == '__main__':
	app.run(debug=True)