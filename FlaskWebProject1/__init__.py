"""
The flask application package.
"""
'''
from flask_cors import CORS, cross_origin
'''
from flask import Flask

app = Flask(__name__)
'''
CORS(app)
'''

import FlaskWebProject1.views
