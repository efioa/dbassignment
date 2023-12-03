from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import sqlite3

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True)
    password = db.mapped_column(db.String(80))

    def __str__(self):
        return self.username


class BlogPost(db.Model):
    id = db.mapped_column(db.Integer, primary_key=True)
    title = db.mapped_column(db.String(100), nullable=False)
    content = db.mapped_column(db.Text, nullable=False)
    created_at = db.mapped_column(db.DateTime, default=datetime.utcnow)
    author_id = db.mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', backref=db.backref('blog_posts', lazy=True))

    def __str__(self):
        return f'"{self.title}" by {self.author.username} ({self.created_at:%Y-%m-%d})'

    @staticmethod
    def get_post_lengths():
        sql = text("SELECT length(title) + length(content) FROM blog_post")
        return db.session.execute(sql).scalars().all() 

    
    db = sqlite3 ()
    connection = sqlite3.connect('countries.db')

    cursor = connection.cursor()

    command1 = ('''CREATE TABLE IF NOT EXISTS country_clicks (country text, clicks interger)''')
    def update_clicks(country):
    # Check if the country exists in the table
    cursor.execute("SELECT * FROM country_clicks WHERE country=?", (country,))

    data = c.fetchone()

    if data is None:
        # If the country doesn't exist, add a new row for it with a click count of 1
        c.execute("INSERT INTO country_clicks (country, clicks) VALUES (?, ?)", (country, 1))
    else:
        # If the country exists, increment the click count by 1
        clicks = data[1] + 1
        c.execute("UPDATE country_clicks SET clicks=? WHERE country=?", (clicks, country))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    'update_clicks()'