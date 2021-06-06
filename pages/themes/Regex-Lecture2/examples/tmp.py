import re

str = "hEBllo this "

# next 2 lines:
# regex = re.compile(r"[aeiouy]+",re.I)
# regex_with_flags_arg= re.compile(r"[aeiouy]+",re.I)
regex_with_flags_prefix= re.compile(r"(?i)[aeiouy]+")

# m = regex_with_flags_arg.findall(str)
m = regex_with_flags_prefix.findall(str)

# are equivalent to:
# m = re.search(r"[aeiouy]+", str, re.I)


print(m)
