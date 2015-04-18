import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['youremail@yourdomain.com'])

SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db').replace('\\','/') #usable on Windows
#SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % ('root', 'psw', 'ip', 'db_name')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"
