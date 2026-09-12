import sqlite3
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "replace-this-with-something-random-later"

def get_db_connection():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    return con

@app.route("/")
def index():
    query = request.args.get("query", "")

    con = get_db_connection()
    if query:
        books = con.execute(
            "SELECT id, title, author, description, user_id FROM books WHERE title LIKE ? OR author LIKE ?",
            (f"%{query}%", f"%{query}%")
        ).fetchall()
    else:
        books = con.execute(
            "SELECT id, title, author, description, user_id FROM books"
        ).fetchall()
    con.close()

    return render_template("index.html", books=books, query=query)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]
    password_hash = generate_password_hash(password)

    con = get_db_connection()
    con.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    con.commit()
    con.close()

    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    con = get_db_connection()
    user = con.execute(
        "SELECT id, username, password_hash FROM users WHERE username = ?",
        (username,)
    ).fetchone()
    con.close()

    if user is None or not check_password_hash(user["password_hash"], password):
        return "Invalid username or password", 401

    session["user_id"] = user["id"]
    session["username"] = user["username"]
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/books/new", methods=["GET", "POST"])
def new_book():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "GET":
        return render_template("new_book.html")

    title = request.form["title"]
    author = request.form["author"]
    description = request.form["description"]

    con = get_db_connection()
    con.execute(
        "INSERT INTO books (user_id, title, author, description) VALUES (?, ?, ?, ?)",
        (session["user_id"], title, author, description)
    )
    con.commit()
    con.close()

    return redirect("/")

@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    if "user_id" not in session:
        return redirect("/login")

    con = get_db_connection()
    book = con.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()

    if book is None:
        con.close()
        return "Book not found", 404

    if book["user_id"] != session["user_id"]:
        con.close()
        return "Not authorized", 403

    if request.method == "GET":
        con.close()
        return render_template("edit_book.html", book=book)

    title = request.form["title"]
    author = request.form["author"]
    description = request.form["description"]

    con.execute(
        "UPDATE books SET title = ?, author = ?, description = ? WHERE id = ?",
        (title, author, description, book_id)
    )
    con.commit()
    con.close()

    return redirect("/")

@app.route("/books/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    if "user_id" not in session:
        return redirect("/login")

    con = get_db_connection()
    book = con.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()

    if book is None:
        con.close()
        return "Book not found", 404

    if book["user_id"] != session["user_id"]:
        con.close()
        return "Not authorized", 403

    con.execute("DELETE FROM books WHERE id = ?", (book_id,))
    con.commit()
    con.close()

    return redirect("/")