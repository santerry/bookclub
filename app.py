from flask import Flask, render_template, request, redirect, session, abort
import config
import books

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    search_query = request.args.get("query")
    book_list = books.get_books(search_query)
    return render_template("index.html", books=book_list, query=search_query)

@app.route("/books/<int:book_id>")
def show_book(book_id):
    book = books.get_book(book_id)
    if not book:
        abort(404)
    return render_template("show_book.html", book=book)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
        abort(403)
    if len(username) > 50 or len(password) > 100:
        abort(403)

    if books.create_user(username, password):
        return redirect("/")
    else:
        return "Username already taken"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    user_id = books.check_login(username, password)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        return redirect("/")
    else:
        return "Invalid username or password"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/books/new", methods=["GET", "POST"])
def new_book():
    require_login()

    if request.method == "GET":
        return render_template("new_book.html")

    title = request.form["title"]
    author = request.form["author"]
    description = request.form["description"]

    if not title or not author:
        abort(403)
    if len(title) > 200 or len(author) > 200:
        abort(403)

    user_id = session["user_id"]
    book_id = books.add_book(title, author, description, user_id)
    return redirect("/books/" + str(book_id))

@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    require_login()

    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_book.html", book=book)

    title = request.form["title"]
    author = request.form["author"]
    description = request.form["description"]

    if not title or not author:
        abort(403)
    if len(title) > 200 or len(author) > 200:
        abort(403)

    books.update_book(book_id, title, author, description)
    return redirect("/books/" + str(book_id))

@app.route("/books/<int:book_id>/delete", methods=["GET", "POST"])
def delete_book(book_id):
    require_login()

    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_book.html", book=book)

    if "continue" in request.form:
        books.remove_book(book_id)
    return redirect("/")
