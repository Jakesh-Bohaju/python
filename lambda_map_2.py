# output :['Hari', 'Shyam' ....] -> ['iraH', 'mayhS' .....]

names = ['Hari', 'Ram', 'Shyam', 'Sita']
reverse = lambda nam: nam[::-1]
reversed_names = list(map(reverse, names))
print(reversed_names)

# output : [2, 3, 5, 9] -> [2, 6, 120, ...] (factorial)

numbers = [2, 3, 5, 9]


def facto(f):
    temp = 1
    for i in range(1, f + 1):
        temp = temp * i
    return temp


print(list(map(facto, numbers)))

# ['Hari' , 'Shyam' ....] -> [4, 5 ...] (number of character)

character = lambda name: len(name)
print(list(map(character, names)))

# ['xyz@gmail.com' ......] -> ['xyz' ....]
emails = ['abc@gmail.com', 'xyz@hotmail.com', 'jkl@gmail.com', 'rty@yahoo.com', 'wes@outlook.com']


def name_extraction(email):
    index_value = email.index('@')
    name = email[:index_value]
    return name


print(list(map(name_extraction, emails)))
