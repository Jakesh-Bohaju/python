a = 0
b = 1
print(b)
for i in range(0, 9):
    num = a + b
    a = b
    b = num
    print(num)
