out_file = '/home/waruna/Documents/projects/pseudo_web/PseudoWebsite/user_code/e3c83258-faab-4716-b106-4c8f850f0979.out'


for i in range(0,100):
        while True:
            try:
                with open(out_file, 'r') as file:
                    output = file.read()
    
            except Exception:
                continue
            break
print output