import requests as r
import json


## GET DATA - NO PARAMETERS
## it will work if no arguments are specified; will return all the data
## it will NOT work if the arguments have been specified
# url = 'http://127.0.0.1:5001/api'
# resp = r.get(url)
# print(resp.json())

## GET DATA - SINGLE PARAMETER
# url = 'http://127.0.0.1:5001/api'
# console = 'Nintendo'
# resp = r.get(f'{url}?console={console}')
# print(resp.json())

# ## POST DATA - VIA ARGUMENTS
# url = 'http://127.0.0.1:5001/save'
# console = 'Nintendo'
# name = 'Mario Maker'
# resp = r.post(f'{url}?console={console}&name={name}')
# print(resp.json())


## POST DATA - VIA JSON
url = 'http://127.0.0.1:5001/saveJSON'
body = {'console': 'Nintendo',
        'name': 'Animal Crossing'}

resp = r.post(url, json=body)
print(resp.json())