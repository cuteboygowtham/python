lists = [100, 200, 300, 400, 500]


def discount(price):
    price = price - (price * 10) / 100
    return price


updatedprices = (list(map(discount, lists)))
print("Without Discount Price : ", lists)
print("With Discount Prices : ", updatedprices)
