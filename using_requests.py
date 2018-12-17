import requests as req

homepage = req.get('http://www.kabmart.com/api/categories')  # in the site json data is access
# print(homepage.content)
json_data = homepage.json()  # .json is for deserialize

print(json_data)
print(json_data[0]['name'])

names = lambda name: name['name']
print(list(map(names, json_data)))
