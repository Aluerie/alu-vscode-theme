"""
* First rename config.example.py into config.py and fill in your VS code installation 
* Second run copy.py if you don't have default themes json files in `./temp/` folder
* Then run build.py to actually build the theme using alu.yaml from `./src/` folder
"""
import json
import yaml

def merge_dicts(dict1, dict2):
    """https://stackoverflow.com/a/7205672/19217368"""
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(merge_dicts(dict1[k], dict2[k])))  # type: ignore
            elif isinstance(dict1[k], list) and isinstance(dict2[k], list):
                yield (k, dict1[k] + dict2[k])
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])

def merge(dict1, dict2):
    return dict(merge_dicts(dict1, dict2))

data = {}  # final dictionary

# make sure you have updated files in `./temp`
default_theme_files = [
    'dark_vs.json', 
    'dark_plus.json' ,
    'dark_plus_experimental.json',
]
for file in default_theme_files:
    f = open(f'./temp/{file}')
    temp = json.load(f)
    data = merge(data, temp)

# my additions
with open("./src/alu.yaml", 'r') as yaml_in:
    temp = yaml.safe_load(yaml_in)
    data = merge(data, temp)
    # reorder data to temp standard
    data = {k: data[k] for k in temp}

data.pop('alu')

# final dump
with open('./themes/alu_dark_pycharm-high-contrast.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
