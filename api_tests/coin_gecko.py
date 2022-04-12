import pandas.io.json
import requests
import json
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
from pandas.io.json import json_normalize

r = requests.get('https://api.coingecko.com/api/v3/global/decentralized_finance_defi')

a = json.loads(r.text)

# res = json_normalize(a)
res = pandas.json_normalize(a)
##print(res)

df = pd.DataFrame(res)
#data = df['pairs'].iloc[0]
print(df)

##df = pd.read_json(a)
##print(df) 