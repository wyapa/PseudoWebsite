import uuid
import os
import subprocess
import json

py_file = './user_code/9f39ca09-638e-444e-82b5-52b620defe84.py'

with open(py_file, 'r') as file:
        test = file.read()

test = test.replace('\n', '/newline')

j = json.dumps(test)
print json.loads(j)