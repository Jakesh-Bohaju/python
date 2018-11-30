# using function definition
names = ['Hari', 'Shyam', 'Rajesh']
formatted_names = []
for name in names:
    namesss = 'Mr ' + name
    formatted_names.append(namesss)
print(formatted_names)

# using lambda function
new_name = []
formatted_namess = lambda names: 'Mr ' + names
for name in names:
    namess = formatted_namess(name)
    new_name.append(namess)
print(new_name)

# using map in list
# map is use for data transfer like "Ram" to "Mr Ram"
# note : map use in case of having only one parameter
# map(function, iteration)
# function must have only one parameter, iteration is of looping i.e use list or tuple
formatted_names = list(map(formatted_namess, names))
print(formatted_names)




names1 = ['Ram Shrestha', 'Jakesh Bohaju', 'Ramesh keumar Sharma']
first_name = lambda names1: names1.split(' ')[0]
first_names = list(map(first_name, names1))
print(first_names)

g_added= lambda names1: names1 + ' ji'
add_g_at_last_of_name = list(map(g_added, names1))
print(add_g_at_last_of_name)

#squaring list element using map and lambda in single line
print(list(map(lambda no: no ** 2, [2, 3, 6, 7])))
