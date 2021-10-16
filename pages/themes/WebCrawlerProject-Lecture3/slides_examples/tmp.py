import requests

# GET request without SSL verification:
r = requests.get(url,verify=False)

# set content encoding explicitely
r.encoding="utf-8"

# get content:
