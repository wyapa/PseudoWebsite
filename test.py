import uuid
import os
import subprocess
import json
import imp
import sys
sys.path.append('./Pseudo/')
import pseudo

psu_path = './user_code/7f59f600-76c1-40ca-821b-4f17f204af79.psu'

psu_path = os.path.abspath(psu_path)


command = 'pseudo.py ' + psu_path

ps = pseudo.main(command)


'''
with open(py_file, 'r') as file:
        test = file.read()

test = test.replace('\n', '/newline')

j = json.dumps(test)
print json.loads(j)

'''