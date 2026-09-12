import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    return con

@app.route("/")
def index():
    con = get_db_connection()
    books = con.execute("SELECT id, title, author, description FROM books").fetchall()
    con.close()
    return render_template("index.html", books=books)