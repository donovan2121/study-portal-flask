import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/students'
    SQLALCHEMY_TRACK_MODIFICATIONS = False