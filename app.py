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
def log():
    return render_template("login.html")

@app.route("/login.html", methods=["POST", "GET"])
def login():
    global l_uname
    l_uname = request.form["uname"]
    l_pswd = request.form["pswd"]
    conn = db_connection()
    cursor = conn.cursor()
    sql = "SELECT uname, pswd from users WHERE uname = '{un}' AND pswd = '{pw}'".format(un = l_uname, pw = l_pswd)
    rows = cursor.execute(sql)
    rows = rows.fetchall()
    if len(rows) == 1:
        return redirect(url_for("homepage"))
    else:
        return redirect(url_for("signup"))
    return render_template("login.html")

@app.route("/signup.html", methods=["POST", "GET"])
def signup():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        # session.permanent = True
        uname = request.form["uname"]
        email = request.form["email"]
        name = request.form["name"]
        pswd = request.form["pswd"]
        # session["uname"] = uname
        sql = """INSERT INTO users (email, uname, name, pswd)
                 VALUES (?, ?, ?, ?)"""
        sqltable = "CREATE TABLE '{un}' (item_id integer PRIMARY KEY AUTOINCREMENT, category text NOT NULL, price FLOAT NOT NULL)".format(un = uname)
        cursor = cursor.execute(sqltable)         
        cursor = cursor.execute(sql, (email, uname, name, pswd))
        conn.commit()
        return redirect(url_for("login"))
    else:
        if "uname" in session:
            return redirect(url_for("homepage"))
    return render_template("signup.html")
    
@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")


@app.route("/expense.html")
def expense():
    return render_template("expense.html")

@app.route("/expense.html", methods=["POST", "GET"])
def expense_data():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        category = request.form["category"]
        price = request.form["price"]
        sql = "INSERT into '{un}' (category, price) VALUES (?, ?)".format(un =l_uname)
        cursor = cursor.execute(sql, (category, price))
        conn.commit()
    return redirect(url_for("homepage"))
    

@app.route("/logout")
def logout():
	session.pop("uname", None)
	return redirect(url_for("login"))

if __name__ == '__main__':
	app.run(debug=True)
