# can add user define index
# user define key and user define value


sample_dict = {'name': 'Bishnu', 'roll': 2}  # here 'name' and 'roll' is key & 'Bishnu' and 2 is value
print(sample_dict['name'])  # print values of respective key
print(sample_dict.get('name'))  # print values of respective key
print(sample_dict.get('father_name', 'Not Given'))  # if key does not include then print 'Not Given'
for key in sample_dict:  # on applying loop key is access
    print('key ->', key, 'value ->', sample_dict[key])

# print(sample_dict['father_name'])  # it give error so in this case use get i.e key is not exist in dictionary

sample_dict['name'] = 'Jakesh'  # change the data of the dictionary of key 'name'
print(sample_dict)

print(sample_dict.keys())  # print keys of dictionary
print(sample_dict.values())  # print values of dictionary

print(sample_dict.items())  # it give tuple inside list

for key, values in sample_dict.items():  # loop to access key and values at a time
    print(key, values)

sample_dict['father_name'] = 'Ram'  # if key not exist add the key to the dictionary
print(sample_dict)
del sample_dict['name']  # delete data of keys defines
print(sample_dict)
sample_dict.popitem()  # delete last key and its value
print(sample_dict)

sam_dict = {'name': ('Jakesh', 'Hari'), 'roll': (2, 4)}
for names in sam_dict['name']:
    print(names)
