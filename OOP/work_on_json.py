import json

data = {'name': 'Bishnu', 'roll': 14, 'phone': 9847092735}
str_version = json.dumps(data)  # Serialize
print(str_version)

with open('json_file', 'w') as json_file:
    json_file.write(str_version)

print(type(str_version))

again_dict = json.loads(str_version)  # deserialize
print(type(again_dict))
