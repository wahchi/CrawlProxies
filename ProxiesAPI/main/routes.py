from flask import Blueprint,jsonify, Flask, request, g, redirect, sessions, url_for, abort, render_template, flash, logging, send_from_directory, send_file, after_this_request
from main import app, mongo
from bson.json_util import dumps
from flask.views import MethodView
from .proxies_view import ProxiesView, ProxyView
proxies_pages = Blueprint('proxies', __name__, template_folder='templates')
class Index(MethodView):
    '''
    Index view for testing
    '''
    def get(self):
        return render_template('hello.html')

#register the urls
proxies_pages.add_url_rule('/', view_func=Index.as_view('index_view'))
proxies_pages.add_url_rule('/proxies', view_func=ProxiesView.as_view('all_proxies'))
proxies_pages.add_url_rule('/proxy/<proxy_address>', view_func=ProxyView.as_view('delete_proxy'))
proxies_pages.add_url_rule('/proxy/<proxy_address>', view_func=ProxyView.as_view('single_proxy'))

