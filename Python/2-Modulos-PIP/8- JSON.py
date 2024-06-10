import json

# 1-Strings para dicionarios

person = '{"name":"Eduardo", "languages": ["Python","JS"]}'
person_dict = json.loads(person)

print(person_dict['languages'])


# Salvando json em txt

# its creating a new file, thats why its using w
with open('person.txt', "w") as json_file:
    json.dump(person_dict,json_file)
