from app import app, db
from app.forms import RegistrationForm, LoginForm
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.models import Student, User
from werkzeug.urls import url_parse
from app.email import send_email, send_student_registration
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin')
@login_required
def admin():
    students = Student.query.all()

    return render_template('admin.html', students=students)

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

        # notify admin via smtp
        # send_student_registration(student)

    return render_template('registration.html', title='Registration Portal', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))  
        login_user(user, remember=form.remember_me.data)
        
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
        
    return render_template('login.html', title='Login Page', form=form)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


