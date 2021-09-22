import re

test_string = '\\stop'
patterns = [
	'\\stop',
	'\\\\stop',
	r'\\stop'
]

for pattern in patterns:
	if re.match(pattern, test_string):
		print(f"Pattern /{pattern}/ MATCHED string {test_string}!")
	else:
		print(f"Pattern /{pattern}/ DID NOT MATCHED string {test_string}!")






# if re.match(re1, text):
# 	# would not match, as '\' is a special character in regex and should be escaped, as well
# 	print(f"/{re1}/ matched {text}!")
# else:
# 	print(f"/{re1}/ DID NOT MATCHED {text}!")

# if re.match(re2, text):
# 	print(f"/{re2}/ matched {text}!")
# else:
# 	print(f"/{re2}/ DID NOT MATCHED {text}!")

# if re.match(re3, text):
# 	print(f"/{re3}/ matched {text}!")
# else:
# 	print(f"/{re3}/ DID NOT MATCHED {text}!")