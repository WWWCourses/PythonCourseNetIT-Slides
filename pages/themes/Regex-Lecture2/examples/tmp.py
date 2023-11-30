import re

test_string = 'a-c,b'

res = re.split(re.compile(r'[-,]'),test_string)
print(res)