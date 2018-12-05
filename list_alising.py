# mutable list
# both a and b point same memory location
# this case only happen in list
# use for memory management
# this called alising

a = [1, 2, 3, 4]

b = a
b.append(5)
print(a)

a.append(6)
print(b)

# in this case just copy the list value of a to c, copy() must called and the location of a and c is different
# use for duplication of list
c = a.copy()
print(c)
print(a)
