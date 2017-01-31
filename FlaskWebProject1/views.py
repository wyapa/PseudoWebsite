"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import json
from flask import request
import uuid
import os
from subprocess import call
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
    jsdata = "HELLO"
    return json.dumps(jsdata)


@app.route('/postmethod', methods = ['POST'])
def postmethod():
    jsdata = request.form['javascript_data']
    name = uuid.uuid4()
    path = './user_code/' + str(name) + '.psu'
    path = os.path.abspath(path)

    with open(path, 'a+') as f:
        f.write(jsdata)
    
    call_string = 'python ../Pseudo/pseudo.py ' + path
    #call([call_string])
   
    return call_string