
class Crawler():
	def __init__(self, seed):
		pass

	def make_filename(self,url):
		""" Extracts domain from a url.
			Prepend data_path and append '.html'

			:param url: string

			return <domain>.html string
		"""
		pass

	def write_to_file(self,filename, content):
		""" Write string to given filename
				:param filename: string
				:param content: sring
		"""
		pass

	def get_html(self,url):
		""" Make GET request and save content to file
			First try with SSL verification (default),
			if error => disable SSL verification

			:param url: string
		"""
		pass


	def run(self):
		""" run the crawler for each url in seed
			Use multithreading for each GET request

		"""
		for url in self.seed:
			self.get_html(url)

if __name__ == '__main__':
	seed = [
		'https://www.autokelly.bg/',
		'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
	]
	crawler = Crawler(seed)
	crawler.run()


