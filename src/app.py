#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tempfile import gettempdir
from flask import Flask, render_template, request, make_response, send_file
from flask_cors import CORS
from url_auth_fs_dav_provider import FilesystemProvider
from wsgidav.wsgidav_app import WsgiDAVApp
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import logging

app = Flask(__name__)
app.config.from_pyfile('../config/server.cfg')
CORS(app, resources={r"/storage/*": {"origins": "*"}})
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("wsgidav")
logger.propagate = True
logger.setLevel(logging.DEBUG)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html", host = request.host)

def start_dav_app():
    root_path = gettempdir()
    provider = FilesystemProvider(root_path)
    config = {
        "provider_mapping": {"/": provider},
        "http_authenticator": {
            "domain_controller": None  # None: dc.simple_dc.SimpleDomainController(user_mapping)
        },
        "error_printer": {"catch_all": True},
        "simple_dc": {"user_mapping": {"*": True}},  # anonymous access
        "verbose": 6,
        "enable_loggers": [],
        "property_manager": True,  # True: use property_manager.PropertyManager
        "lock_manager": True,  # True: use lock_manager.LockManager
    }
    dav_app = WsgiDAVApp(config)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/storage' : dav_app
    })

if __name__ == '__main__':
    start_dav_app()
    app.run(host='0.0.0.0', port=5000)
