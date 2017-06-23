from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask('__name__')
app.config['MONGO_DBNAME'] = 'free_proxies'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/free_proxies'

mongo = PyMongo(app, config_prefix='MONGO')
def register_blueprint():
    from .routes import proxies_pages
    app.register_blueprint(proxies_pages)

register_blueprint()



from . import routes