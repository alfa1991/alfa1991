from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///initiate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)

@app.route('/users/')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    return render_template('user.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц, если их еще нет
    app.run(debug=True)
