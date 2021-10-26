from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

prt = Flask(__name__,instance_relative_config=True) 
csrfobj = CSRFProtect(prt)

from instance import config
prt.config.from_pyfile("config.py")

db = SQLAlchemy(prt)
migrate = Migrate(prt,db) #this will allow us to run migrations using Flask-Migrate

from portfolio.myroutes import user

from . import forms
from . import models 


