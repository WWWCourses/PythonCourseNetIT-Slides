from bs4 import BeautifulSoup as bs

html ="""
	<ul class="menu" id="test" data-note="abc">
		<li><a href="https://somesite.com/page1">page1</a></li>
		<li><a href="https://somesite.com/page2">page2</a></li>
		<li><a href="https://somesite.com/page3">page3</a></li>
	</ul>
"""

soup = bs(html, 'html.parser')

# get first UL element:
first_ul = soup.ul
print(first_ul)

# get all attributes of an element:
first_ul_attributes = first_ul.attrs
print(first_ul_attributes)

# get all text content inside element
for string in first_ul.stripped_strings:
	print(string)

print(first_ul.id)