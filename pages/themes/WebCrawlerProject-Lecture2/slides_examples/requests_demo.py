import requests

def simple_GET_request(url):
	r = requests.get(url);

	print(r.status_code)

def get_without_ssl_verification(url):
	# GET request without SSL verification:
	r = requests.get(url,verify=False)

	# set content encoding explicitely
	r.encoding="utf-8"

	# get content:
