import csv

data_file = open('data.csv', 'r')
reader = csv.DictReader(data_file)
data = list(reader)
data_file.close()  # close file after completion of its operation

# for item in data:
#     # print(dict(item))
#     print('loop 1', item)
#
#
# for item in data:
#     print('loop 2', item)


# only_males = list(filter(lambda item: item['Gender'].lower() == 'male' or item['Gender'].lower() == 'm', data))
# for item in only_males:
#     print(item)

# only_jhapa = list(filter(lambda item: item['Address'].lower() == 'jhapa', data))
# for item_jhapa in only_jhapa:
#     print(item_jhapa)


# below18 = list(filter(lambda item: (2075 - int(item['DOB'].split('-')[0])) < 18, data))
# print(below18)

# only_sharma = list(filter(lambda item: item['Name '].split(' ')[-1].lower() == 'sharma', data))
# for item_sharma in only_sharma:
#     print(item_sharma)

# def mapping_func(item):
#     item['age'] = 2075 - int(item['DOB'].split('-')[0])
#     return item
#
#
# age = list(map(mapping_func, data))
#
# print(age)
#
# # just try
# # below18 = list(map(lambda item: (2075 - int(item['DOB'].split('-')[0])), data))
# # for age in below18:
#
#
# new_file = open('modified.csv', 'w')
# writer = csv.DictWriter(new_file, fieldnames=age[0].keys())
# writer.writeheader()
# writer.writerows(age)
# new_file.close()
#
# # jhapa only
# jhapa_only = list(filter(lambda item: item['Address'].lower() == 'jhapa', data))
# print(jhapa_only)
# jhapa_file = open('jhapa.csv', 'w')
# jhapa_writer = csv.DictWriter(jhapa_file, fieldnames=jhapa_only[0].keys())
# # jhapa_writer = csv.DictWriter(jhapa_file, fieldnames=['DOB])
# jhapa_writer.writeheader()
# jhapa_writer.writerows(jhapa_only)
# jhapa_file.close()


## other approach to write in file
with open('jhapa.csv', 'w') as jhapa_file:
    jhapa_writer = csv.DictWriter(jhapa_file, fieldnames=jhapa_only[0].keys())
    jhapa_writer.writeheader()
    jhapa_writer.writerows(jhapa_only)

# # first, second and last name in different
# first_name = list(map(lambda item : item['Name '].split(' ')[0], data))
# print(first_name)
