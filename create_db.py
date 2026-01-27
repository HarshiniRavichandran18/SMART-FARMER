import sqlite3

db = sqlite3.connect('database.db')
db.execute("CREATE TABLE IF NOT EXISTS vegetables (name TEXT, price INTEGER)")
db.close()

print("Database ready")