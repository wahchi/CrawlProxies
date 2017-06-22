from flask import Blueprint,jsonify, Flask, request, g, redirect, sessions, url_for, abort, render_template, flash, logging, send_from_directory, send_file, after_this_request
from . import app, mongo
from bson.json_util import dumps
from flask.views import MethodView

proxies_pages = Blueprint('proxies', __name__, template_folder='templates')

class Index(MethodView):
    '''
    Index view for testing
    '''
    def get(self):
        return render_template('hello.html')

#register the urls
proxies_pages.add_url_rule('/', view_func=Index.as_view('index_view'))
@app.route('/', methods=['GET'])
def index():
    return render_template('hello.html')

@app.route('/api/v1.0/proxies', methods=['GET'])
def get_proxies():
    '''
    get all proxies
    :return: 
    '''
    try:
        proxies = mongo.db.proxies_info.find()
    except Exception:
        return jsonify({'error': Exception}), 404
    else:
        return dumps(proxies), 200

@app.route('/api/v1.0/proxy/<int:proxy_id>', methods=['DELETE'])
def delete_proxy(proxy_id):
    '''
    delete one proxy
    :return: 
    '''
    try:
        mongo.db.proxies_info.remove({'_id': proxy_id})
    except Exception:
        return jsonify({'error': Exception}), 404
    else:
        return jsonify({'info', 'success'}), 200

@app.route('/api/v1.0/proxies', methods=['PUT'])
def update_proxies():
    pass