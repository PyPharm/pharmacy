"""
Started December 13, 2021
Query example (via SQL statement)
https://data.illinois.gov/api/3/action/datastore_search_sql?sql=SELECT * from "fcccf102-dba5-4a8c-ac07-527779e7e580" WHERE title LIKE 'jones'

Column	Type	Label	Description
License Type	text
Description	text
License Number	text
License Status	text
Business	text
Title	    text
First Name	text
Middle	    text
Last Name	text
Prefix	    text
Suffix	    text
Business Name	text
BusinessDBA	    text
Original Issue Date	text
Effective Date	text
Expiration Date	text
City	text
State	text
Zip	text
County	text
Specialty/Qualifier	text
Controlled Substance Schedule	text
Delegated Controlled Substance Schedule	text
Ever Disciplined	text
LastModifiedDate	text
Case Number	text
Action	text
Discipline Start Date	text
Discipline End Date	text
Discipline Reason	text


https://data.illinois.gov/dataset/professional-licensing/resource/fcccf102-dba5-4a8c-ac07-527779e7e580
"""



from urllib.parse import urlencode, quote_plus, quote

import pandas as pd
import requests
import json
from pprint import pprint
url = 'https://data.illinois.gov/api/3/action/datastore_search?resource_id=fcccf102-dba5-4a8c-ac07-527779e7e580&limit=100&q=name:jones'
url3 = 'https://data.illinois.gov/api/3/action/datastore_search?resource_id=fcccf102-dba5-4a8c-ac07-527779e7e580&limit=100'

#url_all = 'https://data.illinois.gov/api/3/action/datastore_search?resource_id=fcccf102-dba5-4a8c-ac07-527779e7e580&limit=10&q=License%20Type:registered%20pharmacist'
url_all = 'https://data.illinois.gov/api/3/action/datastore_search?resource_id=fcccf102-dba5-4a8c-ac07-527779e7e580&limit=100&q=name:smith'

#fileobj = request.urlopen(url)

r = requests.get(url_all,allow_redirects=True)

data_json = json.loads(r.content)

with open('licenses_2021c.txt', 'w') as outfile:
    json.dump(data_json, outfile)


#df = pd.read_json(data_json)
#print(df.head())

#pprint(data_json['result']['records'])

#pprint(data_json['result']['records'])


#open('download_license.txt', 'wb').write(data_json)

#with open(fileobj) as file:
#    file.write('download.csv')


#print(fileobj.read())

