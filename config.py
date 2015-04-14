import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    globals()
    basedir=basedir
    DEBUG = False
    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'This string will be replaced with a proper key in production.'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 8
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

class DevConfig(BaseConfig):
    DEBUG = True
    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'This string will be replaced with a proper key in production.'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 8
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

class ProductionConfig(BaseConfig):
    DEBUG = False
    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'This string will be replaced with a proper key in production.'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 8
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    RECAPTCHA_OPTIONS = {'theme': 'white'}

class DevTestingConfig(DevConfig):
    TESTING = True

class ProTestingConfig(ProductionConfig):
    TESTING = True