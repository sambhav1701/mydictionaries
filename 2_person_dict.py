person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person['spouse'])

print(person['children'][1])

print(person['pets']['cat'])

for i in person['children']:
   print(i)

for key, value in person['pets'].items():
    print(f"The type of pet is: {key} and the name of the pets is: {value}")