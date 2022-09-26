from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    reddit_username = db.Column(db.String(40))
    course = db.Column(db.String(40))
    response_join = db.Column(db.String(300))
    response_goal = db.Column(db.String(300))
    response_pain = db.Column(db.String(300))
    response_expect = db.Column(db.String(300))

    def __init__(self, reddit_username, course, response_join, response_goal, \
        response_pain, response_expect):

        self.reddit_username = reddit_username
        self.course = course
        self.response_join = response_join
        self.response_goal = response_goal
        self.response_pain = response_pain
        self.response_expect = response_expect

    def __repr__(self):
        return f'<User {self.reddit_username}>'


class User(UserMixin,db.Model):
    __user__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    user_type = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)