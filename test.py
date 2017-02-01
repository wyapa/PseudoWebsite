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
path = './user_code/'
py_path = '/home/waruna/Documents/projects/pseudo_web/PseudoWebsite/user_code/7f59f600-76c1-40ca-821b-4f17f204af79.py'
command = 'pseudo.py ' + psu_path

ps = pseudo.main(command)

command = 'python ' + py_path + ' >> ' + path + '7f59f600-76c1-40ca-821b-4f17f204af79.out'
print command


'''


with open(py_file, 'r') as file:
        test = file.read()

test = test.replace('\n', '/newline')

j = json.dumps(test)
print json.loads(j)

'''