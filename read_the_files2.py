import json

# a Python object (dict):
x = {
   "firstName": "Joe",
   "lastName": "Jackson",
   "gender": "male",
   "age": 28,
   "address": {
       "streetAddress": "101",
       "city": "San Diego",
       "state": "CA"
   },
   "phoneNumbers": [
       { "type": "home", "number": "7349282382" }
   ]
}

# convert into JSON:
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)