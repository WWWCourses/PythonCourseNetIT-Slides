from bs4 import BeautifulSoup

html = """
<body>
    <div>
        <h3>Product 1 title</h3>
        <a href="/products/1">view product1 page</a>
    </div>
    <div>
        <h3>Product 2 title</h3>
        <a href="/products/2">view product2 page</a>
    </div>
    <a href="https://somesite.com/add1">add1</a>
</body>
"""

# Task: get links and h3 heading for all products by selecting a tag which href starts with "/products"
soup = BeautifulSoup(html, 'html.parser')

products_links = soup.select('a[href^="/products"]')

for link in products_links:
    print(link)
    # get h3 as from link's parent div:
    h3 = link.parent.find('h3')
    print(h3)

# <a href="/products/1">view product1 page</a>
# <h3>Product 1 title</h3>
# <a href="/products/2">view product2 page</a>
# <h3>Product 2 title</h3>