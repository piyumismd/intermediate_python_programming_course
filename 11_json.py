
# json - JavaScript Object Notation
# used for data exchange

# convert a python dict to json object

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmeer"]}

import json

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# we can convert this string to a json file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# To convert a json object in to a python dict

person = json.loads(personJSON)
print(person)

# convert from json file

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)

### To convert a class in to a json
# encode custom object with default argument


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# encored with custom json encoder

from json import JSONEncoder


class UserEncoder(JSONEncoder):

   def default(self, o):
       if isinstance(o, User):
           return {"name": o.name, "age": o.age, o.__class__.__name__: True}
       return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

# same as

UserJson = UserEncoder().encode(user)
print(userJSON)


### Decode custom object to python

def decode_user(dct):
    if User.__name__ in dct:
        return User (name=dct["name"], age=dct["age"])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
print(user.age)

