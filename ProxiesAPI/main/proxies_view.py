from flask.views import MethodView
from . import mongo
from flask import jsonify
from bson.json_util import dumps, loads
from utils.crawl_proxies import crawl
import random
class ProxiesView(MethodView):
    def get(self):
        try:
            proxies = mongo.db.proxies_info.find()
        except Exception:
            return jsonify({'error': Exception}), 404
        else:
            return jsonify(dumps(proxies)), 200
    def put(self):
        mongo.db.proxies_info.remove()
        for proxy in crawl():
            mongo.db.proxies_info.insert(proxy)
        return jsonify({'info': 'success'}), 200


class ProxyView(MethodView):
    def get(self):
        count = mongo.db.proxies_info.count()

        proxy = mongo.db.proxies_info.find().limit(-1).skip(int(random.random()*(count+1))).next()
        return jsonify(dumps(proxy)), 200

    def delete(self, proxy_address):
        '''
        delete one proxy
        '''
        try:
            mongo.db.proxies_info.remove({'ip_address': proxy_address})
        except Exception:
            return jsonify({'error': Exception}), 404
        else:
            return jsonify({'info': 'success'}), 200


