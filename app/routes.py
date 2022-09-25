from crypt import methods
from distutils.log import Log
from app.models import Student
from turtle import title
from app.forms import RegistrationForm, LoginForm
from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.forms import RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        student = Student(reddit_username=form.reddit_username.data, course=form.course.data, \
            response_join=form.response_join.data, response_goal=form.response_goal.data, \
            response_pain=form.response_pain.data, response_expect=form.response_expect.data)
        db.session.add(student)
        db.session.commit()
        flash('Registration is Successful!')
    return render_template('registration.html', title='Registration Portal', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('admin.html', title='Admin Panel')
    
    

