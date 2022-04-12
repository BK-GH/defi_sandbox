import pandas.io.json
import requests
import json
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
from pandas.io.json import json_normalize

r = requests.get('https://api.dexscreener.io/latest/dex/search?q=0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd')

a = json.loads(r.text)

# res = json_normalize(a)
res = pandas.json_normalize(a)
##print(res)

df = pd.DataFrame(res)
data = df['pairs'].iloc[0]
print(data)

##df = pd.read_json(a)
##print(df)