import json

prices = {
    "apples":2.50,
    "bananas":1.80,
    "strawberry": 3.20
}

with open('json_dump.out', 'w+') as fh:
    json.dump(prices, fh, indent=4)