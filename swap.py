# using two variable
# x = int(input('Enter x value'))
# y = int(input('Enter y value'))
#
# x = x + y
# y = x - y
# x = x - y
# print("X : ",x)
# print("Y : ",y)


# using 3 variable
# x = int(input('Enter x value'))
# y = int(input('Enter y value'))

# z = x
# x = y
# y = z


x = int(input('Enter x value'))
y = int(input('Enter y value'))
x, y = y, x  # swap direct in python, multiple assigning

print("X : ", x)
print("Y : ", y)
