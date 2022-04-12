import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
import requests
from dune_analytics import Dune
from keys.dune_keys import *

dune = Dune(dune_username, dune_password)
dune.login()

results = dune.query('''
    select 
    to_char(block_time, 'YY MM-DD') as period, 
    case when token_a_symbol = 'TRIBE' then 'inflows' else 'outflows' end as flow,
    sum(usd_amount) as volume,
    count(*) as trxns
    from dex."trades"
    where (token_b_symbol = 'TRIBE'
                or token_a_symbol = 'TRIBE')
            and "category" = 'DEX'
            and token_b_amount_raw > 0
            and token_a_amount_raw > 0
            and block_time >= '2021-12-15 00:00'
            and project = 'Uniswap'
            and version = '2'
        group by 1, 2
''')

print(results)