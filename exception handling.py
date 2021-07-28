def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Ur divided by Zero")
        return 0

x = float(input("enter a value"))
y = float(input("enter a value"))
rsults = divide(x, y)
print(rsults)


