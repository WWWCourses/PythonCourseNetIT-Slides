import re

# march strings containing word-chars followed by digits:
strings = [
	'petrov42', # ok
	'42petrov',	# not ok (no digits after letters)
	'ivan_pterov2' # ok ('_' is a word character)
]
rx = re.compile('\w+\d+')

for string in strings:
	match = rx.search(string);
	if match:
		print(f"{match[0]} matched in {string}" )
