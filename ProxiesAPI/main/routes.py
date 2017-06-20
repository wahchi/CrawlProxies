from flask import jsonify, Flask, request, g, redirect, sessions, url_for, abort, render_template, flash, logging, send_from_directory, send_file, after_this_request
from . import app

@app.route('/', methods=['GET'])
def index():
    return render_template('hello.html')