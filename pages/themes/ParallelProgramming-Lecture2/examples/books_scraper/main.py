import requests
from bs4 import BeautifulSoup
import time
import threading

# URL of the site to scrape
BASE_URL = 'http://books.toscrape.com/'
# pages to be scraped
PAGES_COUNT = 5

# Function to fetch and parse a page
def fetch_page(url):
    print(f"Fetching {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [a.get_text() for a in soup.select('h3 > a')]
    print(f"Fetched {len(titles)} titles from {url}")
    return titles

# Sequential scraping function
def scrape_sequential(urls):
    titles = []
    for url in urls:
        titles.extend(fetch_page(url))
    return titles

# Threaded scraping function
def scrape_threaded(urls):
    titles = []
    threads = []

    def fetch_and_store(url):
        titles.extend(fetch_page(url))

    for url in urls:
        thread = threading.Thread(target=fetch_and_store, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return titles

# Generate URLs to scrape (using the first 5 pages as an example)
urls = [f'{BASE_URL}/catalogue/page-{i}.html' for i in range(1, PAGES_COUNT+1)]

# Measure time for sequential scraping
print("Starting sequential scraping...")
start_time = time.time()
sequential_titles = scrape_sequential(urls)
sequential_time = time.time() - start_time

# Measure time for threaded scraping
print("Starting threaded scraping...")
start_time = time.time()
threaded_titles = scrape_threaded(urls)
threaded_time = time.time() - start_time

# Display results
print(f'\nSequential scraping took {sequential_time:.2f} seconds and found {len(sequential_titles)} titles.')
print(f'\nThreaded scraping took {threaded_time:.2f} seconds and found {len(threaded_titles)} titles.')
