"""
* First rename config.example.py into config.py and fill in your VS code installation 
* Second run copy.py if you don't have default themes json files in `./temp/` folder
* Then run build.py to actually build the theme using alu.yaml from `./src/` folder
"""
import json
import os
import config

default_theme_files = [
    'dark_vs.json', 
    'dark_plus.json' ,
    'dark_plus_experimental.json',
    'hc_black.json'
]

out_temp = "./temp"

if not os.path.isdir(out_temp):
    os.mkdir(out_temp)

my_files = [f'{config.default_theme_dir}/{i}' for i in default_theme_files]

# copy into `./assets`` folder`
for file in my_files:
    f = open(file)
    temp = json.load(f)
    basename = os.path.basename(f.name)

    # un-minify them as well
    with open(f'{out_temp}/{basename}', 'w', encoding='utf-8') as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)