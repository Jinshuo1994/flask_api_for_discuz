#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app
from exts import db
from models.models_member_forum import *
from models.models_pm import *
from models.models_pm_dynamic import *

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run();