import json
env_configs = []

class TypeMismatch(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.message = msg

with open('dev.json','r') as f:
    dev = json.load(f)

merge = dev.copy()

with open('prod.json','r') as f:
    prod = json.load(f)
    env_configs.append(prod)

with open('staging.json','r') as f:
    staging = json.load(f)
    env_configs.append(staging)

for env in env_configs:
    for section in env.keys():
        try:
            for key in env[section].keys():
                try:
                    if section=='database' and key=='port':
                        merge[section][key] = int(env[section][key])
                        raise TypeMismatch("database.port (int vs string)")
                except TypeMismatch as e:
                    print(f'Type Mismatch: {e}')
                    continue
                merge[section][key] = env[section][key]
        except AttributeError as e:
            merge[section] = list(set(env[section]).union(set(merge[section])))
            print('Conflict Resolved: cache merged as union')

with open('merge.json','w') as f:
    json.dump(merge,f,indent=4)