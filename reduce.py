# reduce must have two parameters
# convert list item to single item

from functools import reduce

print(reduce(lambda a, b: a + b, [2, 4, 10, 16, 20]))



# factorial using lambda and reduce

factorial = lambda no: reduce(lambda a, b: a * b, range(1, no + 1))
print(factorial(5))
