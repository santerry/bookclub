CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    description TEXT
);