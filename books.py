import sqlite3
import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    password_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return False
    return True

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None
    user = result[0]
    if check_password_hash(user["password_hash"], password):
        return user["id"]
    return None

def get_books(search_query=None):
    if search_query:
        sql = """SELECT id, title, author, description, user_id
                 FROM books
                 WHERE title LIKE ? OR author LIKE ?
                 ORDER BY id DESC"""
        like = "%" + search_query + "%"
        return db.query(sql, [like, like])
    sql = "SELECT id, title, author, description, user_id FROM books ORDER BY id DESC"
    return db.query(sql)

def get_book(book_id):
    sql = "SELECT id, title, author, description, user_id FROM books WHERE id = ?"
    result = db.query(sql, [book_id])
    return result[0] if result else None

def add_book(title, author, description, user_id):
    sql = """INSERT INTO books (title, author, description, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, author, description, user_id])
    return db.last_insert_id()

def update_book(book_id, title, author, description):
    sql = """UPDATE books SET title = ?, author = ?, description = ?
             WHERE id = ?"""
    db.execute(sql, [title, author, description, book_id])

def remove_book(book_id):
    sql = "DELETE FROM books WHERE id = ?"
    db.execute(sql, [book_id])
