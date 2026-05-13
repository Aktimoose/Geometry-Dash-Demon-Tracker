#!/usr/bin/env python

import requests
import pyperclip

# puts the gd server response in a dictionary
def parse_gd_response(response_text):
    # levels are separated from creators by # and levels themselves are separated by | and data is separated by :
    main_content = response_text.split('#')[0]
    first_level = main_content.split('|')[0]
    parts = first_level.split(':')
    
    # maps the data to a dictionary
    level_data = {}
    for i in range(0, len(parts) - 1, 2):
        key = parts[i]
        value = parts[i + 1]
        level_data[key] = value

    return level_data

def get_creator_name(response_text, creator_id):
    # creators are separated from levels by # and creators themselves are separated by | and data is separated by :
    creator_content = response_text.split('#')[1]
    creators = creator_content.split('|')
    parts = creators[0].split(':')

    return parts[1] # userid:name:accountid so name is index 1

input_id = input("enter id or level name (id preferred): ")

headers = {
    "User-Agent": ""
}

data = {
    "str": input_id,
    "star": 1,
    "diff": -2,
    "type": 0,
    "secret": "Wmfd2893gb7",
}

url = "http://www.boomlings.com/database/getGJLevels21.php"

req = requests.post(url=url, data=data, headers=headers)
req.raise_for_status()

# puts the gd server response in a dictionary
level_data = parse_gd_response(req.text)

level_id = level_data.get('1')
level_name = level_data.get('2')
demon_diff_num = level_data.get('43')

level_creator_id = level_data.get('6')
level_creator = get_creator_name(req.text, level_creator_id)

# demon difficulty map
demon_diff_map = {
    "3": "Easy",
    "4": "Medium",
    "0": "Hard",
    "5": "Insane",
    "6": "Extreme"
}
demon_diff = demon_diff_map.get(demon_diff_num, "idk")

if level_data.get('15') == "5": # if length is Plat then it's Platformer
    game_type = "Platformer"
else: 
    game_type = "Classic"

pyperclip.copy(f'{level_id}\t{level_name}\t{level_creator}\t{demon_diff}\t\t{game_type}')
