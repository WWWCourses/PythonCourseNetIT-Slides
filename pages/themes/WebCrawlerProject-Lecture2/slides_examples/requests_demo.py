import requests
import re

def make_filename(url):
	"""
		Extracts domain from a url and append '.html'

		:param url: string

		return <domain>.html string
	"""
	rx = re.compile(r'^https?:\/\/(?:www.)?([^\/]+)\/?')
	m = rx.search(url)
	if m:
		return m[1]  + '.html'
	else:
		print(f'Can not get domain from {url}')
		exit(0)

def write_to_file(filename, content):
	"""
		Write string to given filename
			:param filename: string
			:param content: sring
	"""
	try:
		with open(filename, 'w') as f:
			f.write(content)
	except FileNotFoundError:
		print(f'File {filename} does not exists!')
	except Exception as e:
		print(f'Ooops, something went wrong ({e.__class__})')

def simple_GET_request(url):
	r = requests.get(url);

	print(r.status_code, r.ok)
	if r.ok:
		filename = make_filename(url)
		write_to_file(filename, r.text)


def get_without_ssl_verification(url):
	# GET request without SSL verification:
	r = requests.get(url,verify=False)

	# set content encoding explicitely
	r.encoding="utf-8"

	# get content:

if __name__ == '__main__':
	print(make_filename('https://test'))
	exit(0)
	seed = [
		'https://www.autokelly.bg/',
		# 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
	]
	for url in seed:
		simple_GET_request(url)

