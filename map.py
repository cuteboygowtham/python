def add(x):
    return x+2

lists = [10, 20, 30, 40, 50]

print(list(map(add, lists)))

#or

print(list(map(lambda y : y*2, lists)))