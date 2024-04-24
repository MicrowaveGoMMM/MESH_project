import requests
import yaml
import json


URL = 'https://sky.shiiyu.moe/api/v2/profile/MicrowaveGoMMM/'
response = requests.get(URL)
main = response.json()
with open('player_endpoint.txt', 'w') as f:
    json.dump(main, f, sort_keys=True, indent=4)
print('done')