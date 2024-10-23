# app.py

from flask import Flask
from config import Config
from database import db, init_db
from models import User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to the User Management App!"

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
