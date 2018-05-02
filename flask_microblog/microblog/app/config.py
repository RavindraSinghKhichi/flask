import os

basedir=os.path.abspath(os.path.dirname(__file__))
#basedir=os.getcwd()

#here we are seting object based configuration for our flask app
'''object based configuration'''
class  Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
