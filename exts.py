from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config
import common.scheduled_work

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(config)
