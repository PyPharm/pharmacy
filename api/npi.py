# Retrieve NPI information from the NPPES NPI Registry API
import requests
import json

base_url = 'https://npiregistry.cms.hhs.gov/api/'

params1 = {'last_name':'limog*',
          'first_name':'dan*'
           }

params2 = {'organization_name':'st. bernar*'}

def clean_nppes_lookup( **kwargs):
    if 'version' not in kwargs.keys():
        kwargs['version'] = '2.1'
    return kwargs

params = clean_nppes_lookup(**params1)

x = requests.get(base_url, params=params)
print(x)
print(x.text)

x = x.json()

print(json.dumps(x['results'], indent=4))