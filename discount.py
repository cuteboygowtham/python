def studentdiscount(price):
    price = price - (price * 10) / 100
    return price


def additionaldiscount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice


sellingprice = float(input("enter selling Price"))

print(studentdiscount(additionaldiscount(sellingprice)))
