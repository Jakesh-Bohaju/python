sample_set = {1, 0, 13, 'x', 'aa', 'a'}
print(sample_set)

a = {2, 5, 3, 4}
b = {3, 10}
c = {0, 1, 9}
d = {2, 5}
print(a.intersection(b))
print(a.difference(b))
print(a.union(b))
print(b.difference(a))
print(a - b)
print(b - a)
print(a.isdisjoint(b))
print(a.issuperset(b))
print(a.issubset(b))
print(a.isdisjoint(c))
print(a.issuperset(c))
print(a.issubset(c))
print(a.isdisjoint(d))
print(a.issuperset(d))
print(a.issubset(d))
print(d.issubset(a))
print(3 in a)
a.add(20)
print(a)
a.remove(2)
print(a)
