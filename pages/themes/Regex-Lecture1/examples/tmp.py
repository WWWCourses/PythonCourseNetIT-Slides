import re

user_pass = "qazwsxedc";

#the pattern to find if the user_pass contains at least 8 symbols:
pattern = r"^.{8,}$";

# do the test:
match = re.search(pattern,user_pass)

if match:
	print("Match")
else:
	print("No match!")