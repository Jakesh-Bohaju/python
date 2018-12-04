a = (3, 1, 2)
b = (1,)
c = 1, 2, 3, 4, 5
d = 5,
z, x = 3, 2  # multiple assignment
a * 2
(3, 1, 2, 3, 1, 2)
a + b
(3, 1, 2, 1)
a[2]
2
a[:-1]
(3, 1)
a[::-1]
(2, 1, 3)

# cant change the value of tuple, immutable
sample_tuple = (3, 2, 5)

a_list = list(sample_tuple)
b_tuple = tuple(a_list)

# list argument, dy default args is tuple
# * use to collect all data
from functools import reduce
def sum(*args):
    # print(args)
    return reduce(lambda a, b: a + b, args)

# sum(2,5,6,7,8,3,2)
print(sum(2, 5, 6, 7, 8, 3, 2))
