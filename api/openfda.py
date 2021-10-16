
# https://open.fda.gov/apis/
# https://open.fda.gov/apis/drug/ndc/searchable-fields/

# With no API key: 240 requests per minute, per IP address. 1,000 requests per day, per IP address.
# With an API key: 240 requests per minute, per key. 120,000 requests per day, per key.


import requests
from requests import Request, Session, HTTPError
import urllib.parse

url_openfda_label = 'https://api.fda.gov/drug/label.json'
url_openfda_ndc = 'https://api.fda.gov/drug/ndc.json'
url_openfda_drugevents = 'https://api.fda.gov/drug/event.json'
api_key = '' #include before all other parameters, even the

url_basic = 'https://api.fda.gov'

params = dict(
   # api_key = api_key
   # ,search = ''
    finished = 'true'
    ,limit = 1

)

def get_ndc_data(params):
    data = requests.get(url_openfda_ndc,params = params).json()

    print(data)

    #for result in data.get('results',[]):
    #    print(result)

    #print(req)

def test():
    URL2 = r'https://api.fda.gov/drug/event.json?search=receivedate:[20160101+TO+20160103]&count=receivedate'
    URL2a = r'https://api.fda.gov/drug/event.json'
    params2b = {
        'search': r'receivedate:[20160101+TO+20160105]'
        ,'count': r'receivedate'
        ,'limit': '5'
    }

    approach = 4

    if approach == 1:
        data2 = requests.get(URL2).json()
        print(data2)
        for result in data2.get('results', []):
            print(result)
    elif approach == 2:
        data2 = requests.get(URL2a, params=params2b).json()
        print(data2)
        for result in data2.get('results', []):
            print(result)
    elif approach == 3:
        prepped = requests.Request("GET", url=URL2).prepare()
        s = requests.Session()
        print (f'Prepped URL: {prepped.url}\nPrepped body: {prepped.body}')

        data2 =  s.send(prepped).json()
        #print(data2.content)
        for result in data2.get('results', []):
            print(result)
    elif approach == 4:
        payload_str = urllib.parse.urlencode(params2b, safe=':+')
        prepped = requests.Request("GET", url=URL2a, params=payload_str).prepare()
        s = requests.Session()
        print (f'Prepped URL: {prepped.url}\nPrepped body: {prepped.body}')

        data2 =  s.send(prepped).json()
        #print(data2.content)
        for result in data2.get('results', []):
            print(result)

def _main(config_file = None):
    test()
    #get_ndc_data(params)


if __name__ == "__main__":
    _main()