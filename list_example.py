sample_list = [1, 2, 3]
b = ['Ram', 'Hari', 'Shyam', 'Gita', 'Sita']
c = [4.5, 5, 9, 'Ram']

b.append("Ramesh")
print(b)
b.insert(2, 'Jakesh')
print(b)
b.sort()
print(b)
b.remove("Jakesh")
print(b)
del b[0]
print(b)
deleted_item = b.pop()
print(b, deleted_item)
deleted_item = b.pop(2)
print(b, deleted_item)

for name in b:
    print(name
          )

d = [1, 2, 3, 1, 4, 5, 6, 1, 2, 4]
print(d.count(1))
print(d.index(1,3))
print(d.index(1,5))


print("Ramesh" in b)




















"""
homogeneous and heterogeneous list
list slicing
append
insert
remove
del
pop
count
index
insert

"""