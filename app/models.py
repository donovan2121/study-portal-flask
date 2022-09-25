from app import db

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