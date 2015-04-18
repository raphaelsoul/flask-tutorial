from flask import Flask, render_template,make_response
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.login import LoginManager
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

#plugins
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

loginmanager = LoginManager()
loginmanager.init_app(app)


'''
def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.
    """
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)
'''

@app.route('/')
def index():
	return make_response('hello,world')

@app.errorhandler(404)
def not_found(error):
	return render_template('errors/404.html'), 404

@app.errorhandler(401)
def not_authorized(error):
	return render_template('errors/401.html'),401

from apps.Account.views import bp_user as usersModule
app.register_blueprint(usersModule)