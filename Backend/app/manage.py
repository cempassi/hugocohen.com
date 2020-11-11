from . import create_app
from flask_script import Command
from flask_migrate import MigrateCommand, Manager

class Init_Admin(Command):
    def run(self):
        from .models.Admin import Administrator
        Administrator.init()

manager = Manager(create_app)
manager.add_command('init_admin', Init_Admin)

if __name__ == '__main__' :
    manager.run()
