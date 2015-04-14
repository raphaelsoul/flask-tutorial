from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

if not app.config['DEBUG']:
	#install_secret_key(app)
	pass

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from apps.UserManage.views import bp_user as usersModule
app.register_blueprint(usersModule)