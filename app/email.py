from flask import render_template
from flask_mail import Message
from app import app, mail
from threading import Thread



def senc_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipient, text_body):
    msg = Message(subject, sender=sender, recipients=recipient)
    msg.body = text_body
    mail.send(msg)


def send_student_registration(student):
    send_email('Student Application', 
                sender = app.config['MAIL_ADMIN'],
                recipient= app.config['MAIL_USERNAME'],
                text_body='test')
