# filter ( boolean_function, iterable)
# boolean_function -> function return either true or false, example 2+3>6
# filter; if return true added to list else discard

# check either no is even
print(list(filter(lambda no: no % 2 == 0, [3, 7, 8, 13, 2])))

# extract name with middle name
names = ['Ram prashad sharma', 'Jakesh Bohaju', 'Sita shrestha']
print(list(filter(lambda name: name.count(' ') > 1, names)))
print(list(filter(lambda name: len(name.split(' ')) > 2, names)))

# print palindrom
words = ['amma', 'hajs', 'hard drah']
print(list(filter(lambda word: word == word[::-1], words)))

# filter gmail only
emails = ['abc@gmail.com', 'xyz@hotmail.com', 'jkl@gmail.com', 'rty@yahoo.com', 'wes@outlook.com']
print(list(filter(lambda email: '@gmail' in email, emails)))
print(list(filter(lambda email: email.count('@gmail') == 1, emails)))


# print perfect square number only

from math import sqrt

numbers = [49, 4, 13, 51, 15, 121, 9, 25]
print(list(filter(lambda number: sqrt(number) == int(sqrt(number)), numbers)))
