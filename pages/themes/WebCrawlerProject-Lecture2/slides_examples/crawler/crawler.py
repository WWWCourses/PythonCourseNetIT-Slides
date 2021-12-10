import requests
import re
import threading
from bs4 import BeautifulSoup as bs

class Crawler():
	def __init__(self, seed):
		self.seed = seed
		self.data_path = './data/'

	def make_filename(self,url):
		""" Extracts domain from a url.
			Prepend data_path and append '.html'

			:param url: string

			return <domain>.html string
		"""
		rx = re.compile(r'^https?:\/\/(?:www.)?([^\/]+)\/?')
		m = rx.search(url)
		if m:
			return self.data_path + m[1]  + '.html'
		else:
			print(f'Can not get domain from {url}')
			exit(0)

	def write_to_file(self,filename, content):
		""" Write string to given filename
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

	def get_html(self,url):
		# GET request without SSL verification:
		try:
			r = requests.get(url)
		except requests.RequestException:
			# try with SSL verification disabled.
			# this is just a dirty workaraound
			# check https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f
			r = requests.get(url,verify=False)

		# set content encoding explicitely
		r.encoding="utf-8"

		# if we have the html => save it into file
		if r.ok:
			filename = self.make_filename(url)
			self.write_to_file(filename, r.text)

			self.extract_links(r.text)

	def extract_links(self, html):
		# create BeautifulSoup object, which represents the document as a nested data structure:
		soup = bs(html, 'html.parser')

		# get HTML element:
		print(soup.title)

		# # get HTML element's content as string:
		print(soup.title.string)

		articles = soup.find("div",id="module_1_1")
		print(articles)

	def run(self):
		for url in self.seed:
			tr = threading.Thread(target=self.get_html(url))
			tr.start()

if __name__ == '__main__':
	seed = [
		# 'https://www.autokelly.bg/',
		# 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
		'https://bnr.bg/hristobotev/radioteatre/list'
	]
	crawler = Crawler(seed)
	crawler.run()


