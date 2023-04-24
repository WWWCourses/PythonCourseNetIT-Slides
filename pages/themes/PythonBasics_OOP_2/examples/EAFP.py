prices = {"apples": 2.5, "oranges": 1.80}
# Pythonic:
# try:
#     print(prices["bananas"])
# except KeyError:
#     print("Key error")

#non-pyhtonic:
if "bananas" in prices:
  print( prices["bananas"] )
