items = [
    ("product1", 1),
    ("product3", 3),
    ("product2", 2),
]

def get_price(item):
    return item[1]

items.sort(key=get_price)
print(items)
