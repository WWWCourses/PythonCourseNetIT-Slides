from bs4 import BeautifulSoup as bs

with open('./test.html', 'r') as f:
	html = f.read()

# create BeautifulSoup object, which represents the document as a nested data structure:
soup = bs(html, 'html.parser')
# print(dir(soup))

# get first UL element:
first_ul = soup.ul
# print(first_ul)

# get all attributes of an element:
first_ul_attributes = first_ul.attrs
# print(first_ul_attributes)

# get text content of an element:
print(soup.title.string)
print(first_ul.string)
print(first_ul.stripped_strings)
for string in first_ul.stripped_strings:
	print(string)


# get all UL elements:
uls = soup.find_all('ul')

# get first UL element with class="menu"
ul_menu = soup.find('ul', class_="menu")
# print(ul_menu)

# get all A elements inside ul.menu:
ul_menu_links = ul_menu.find_all('a')
# print(ul_menu_links)
