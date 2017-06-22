from flask import Flask
from flask.ext.pymongo import PyMongo
from . import routes
app = Flask('__name__')
app.register_blueprint(routes.proxies_pages)

app.config['MONGO_DBNAME'] = 'free_proxies'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/free_proxies'

mongo = PyMongo(app, config_prefix='MONGO')

