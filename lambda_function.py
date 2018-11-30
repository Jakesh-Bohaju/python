def check_even_or_odd(number):
    return number % 2 == 0


another_check_even_or_odd = lambda number: number % 2 == 0

print(check_even_or_odd(7))
print(check_even_or_odd(6))
print(another_check_even_or_odd(7))
print(another_check_even_or_odd(6))


def add(a, b):
    return a + b


print(add(5, 7))

another_add = lambda a, b: a + b

print(another_add(5, 7))


#reverse list
reverse_string = lambda name: name[::-1]
print(reverse_string('ram'))

# add Mr before name
change_name = lambda name: 'Mr ' + name
print(change_name('Ram'))

# print first name using lambda function / inline function
first_name = lambda name: name.split(' ')[0]
print(first_name('Jakesh Bohaju'))
