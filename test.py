import json
out_file = '/home/waruna/Documents/projects/pseudo_web/PseudoWebsite/user_code/e3c83258-faab-4716-b106-4c8f850f0979.out'
py_file = '/home/waruna/Documents/projects/pseudo_web/PseudoWebsite/user_code/e3c83258-faab-4716-b106-4c8f850f0979.py'

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




for i in range(0,100):
    while True:
        try:
            with open(out_file, 'r') as file:
                output = file.read()

        except Exception:
            continue
        break



    


python_code = python_code.replace('\n', '&&newline&&')
output = output.replace('\n', '&&newline&&')

data['python'] = python_code
data['output'] = output
print json.dumps(data)
    