stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total = {}
for key, value in stock.items():
    if key in prices:
        total[key] = prices[key] * stock[key]
print(total)

