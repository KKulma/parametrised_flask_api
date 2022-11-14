import requests as r
url = 'http://127.0.0.1:5001/api'

## NO PARAMETERS
## it will work if no arguments are specified; will return all the data
## it will NOT work if the arguments have been specified
# resp = r.get(url)
# print(resp.json())


## WITH A SINGLE PARAMETERS
console = 'Nintendo'
resp = r.get(f'{url}?console={console}')
print(resp.json())

#
# ## WITH MULTIPLE PARAMETERS
# console = 'Nintendo'
# name = 'Mario Maker'
# resp = r.get(f'{url}?console={console}&name=')
