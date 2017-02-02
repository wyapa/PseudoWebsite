"""
Routes and views for the flask application.
"""
from __future__ import absolute_import
from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import json
from flask import request
import uuid
import os
from flask import jsonify
import sys
import subprocess



@app.route('/')
def spalsh():
	return render_template(
        'splash.html',
        title='Home Page',
    )
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
    data = {}
    path = './user_code/' + str(name) 
    py_file = path + '.py'
    psu_file = path + '.psu'
    out_file = path + '.out'
    psu_file = os.path.abspath(psu_file)
    py_file = os.path.abspath(py_file)
    out_file = os.path.abspath(out_file)
    with open(psu_file, 'a+') as f:
        f.write(jsdata)
    
    
    command = 'python ./Pseudo/pseudo.py ' + str(psu_file)

    '''
    os.system(command)
    '''
    prog = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    data = {}
    
    

    
    for i in range(0,100):
        while True:
            try:
                with open(py_file, 'r') as file:
                    python_code = file.read()
            except Exception:
                continue
            break

    
    
    command = 'python ' + py_file + ' >> ' + out_file
    
    prog = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    





    for i in range(0,100):
        while True:
            try:
                with open(out_file, 'r') as file:
                    output = file.read()
                if output == "":
                    continue
            except Exception:
                continue
            break
    
    
       

    
    python_code = python_code.replace('\n', '&&newline&&')
    output = output.replace('\n', '&&newline&&')

    data['python'] = python_code
    data['output'] = output
    return json.dumps(data)
    
    '''
    data['python'] = py_file
    data['output'] = python_code
    return json.dumps(data)
    '''