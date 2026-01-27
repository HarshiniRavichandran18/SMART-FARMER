from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)  # MUST be here before any @app.route

# Connect to DB
def get_db():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    return db

# Home page
@app.route('/')
def home():
    db = get_db()
    cur = db.execute("SELECT * FROM vegetables")
    vegetables = cur.fetchall()
    db.close()
    return render_template('index.html', vegetables=vegetables)

# Admin panel
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        db.execute("INSERT INTO vegetables (name, price) VALUES (?, ?)", (name, price))
        db.commit()

    cur = db.execute("SELECT * FROM vegetables")
    vegetables = cur.fetchall()
    db.close()
    return render_template('admin.html', vegetables=vegetables)

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()