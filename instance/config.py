import os
from os import environ,path
from dotenv import load_dotenv

basedir=path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))
SECRET_KEY=os.urandom(32)
# SECRET_KEY=environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI= 'mysql+mysqlconnector://root@localhost/portfolio'
SQLALCHEMY_TRACK_MODIFICATIONS=True




