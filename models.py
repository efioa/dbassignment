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

    
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create the 'country_clicks' table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS country_clicks (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    clicks INTEGER NOT NULL
)
""")

# Commit the changes to the database
conn.commit()

def add_country_click(country):
    c.execute("SELECT * FROM country_clicks WHERE country=?", (country,))
    rows = c.fetchall()

    if len(rows) == 0:
        c.execute("INSERT INTO country_clicks (country, clicks) VALUES (?, ?)", (country, 1))
    else:
        c.execute("UPDATE country_clicks SET clicks=? WHERE country=?", (rows[0][1] + 1, country))

    conn.commit()

def country_clicks(country):
    c.execute("SELECT * FROM country_clicks WHERE country=?", (country,))
    rows = c.fetchall()
    click_count = 0

    for row in rows:
        click_count += row[1]

    return click_count

# Example usage:
add_country_click('United States')
add_country_click('United States')
add_country_click('Canada')
print(country_clicks('United States')) # Output: 2
print(country_clicks('Canada')) # Output: 1
