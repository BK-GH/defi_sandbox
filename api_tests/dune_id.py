from duneanalytics import DuneAnalytics
from keys.dune_keys import *

dune = DuneAnalytics(dune_username, dune_password)
dune.login()
dune.fetch_auth_token()

result_id = dune.query_result_id(query_id=589902)

data = dune.query_result(result_id)

print(data)