"""def function(x):
    counter = 0
    while counter < x:
        yield counter
        counter += 1


for y in function(5):
    print(y)
"""


# print even using generators

def even(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even(20)))

"""
# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

    # Create a generator object


x = fib(5)

# Iterating over the generator object using next
print(x)  # In Python 3, __next__()

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(26):
    print(i)"""
