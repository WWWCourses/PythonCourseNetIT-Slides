import re

''' Description:
	Password must follow next rules:
	1. Must contain at least eight characters (no constraints on them)
	2. Must contain at least one letter and one number:

	Tip:
		We may use positive lookahead (https://www.regular-expressions.info/lookaround.html), to test for second condition
'''
def validate_password(string):
	rx = re.compile(r'''(?xi)
	(?=.*\d) 		# test for number, anywhere in string
	(?=.*[a-z])		# test for letter, anywhere in string
	.{8,}			# test for length (all characters)
	''')

	m = rx.search(string)
	if m:
		print(f'{string} is valid!')
	else:
		print(f'{string} is NOT valid!')


passwords = [
	"___a_____1", #yes
	"___1_____a", #yes
	"___1_____!", # no (no letter)
	"_____1a", #no ( Rule 1)
]

for t in passwords:
	validate_password(t)