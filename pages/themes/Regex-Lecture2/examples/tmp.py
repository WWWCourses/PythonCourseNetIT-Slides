import re

text = '\\stop'
re1 = '\\stop'
re2 = '\\\\stop'
re3 = r'\\stop'

if re.match(re1, text):
	# would not match, as '\' is a special character in regex and should be escaped, as well
	print(f"/{re1}/ matched {text}!")
else:
	print(f"/{re1}/ DID NOT MATCHED {text}!")

if re.match(re2, text):
	print(f"/{re2}/ matched {text}!")
else:
	print(f"/{re2}/ DID NOT MATCHED {text}!")

if re.match(re3, text):
	print(f"/{re3}/ matched {text}!")
else:
	print(f"/{re3}/ DID NOT MATCHED {text}!")