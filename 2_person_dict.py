from ctypes import cast


person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)
#print(type(person["children"]))
#print(person['children'][1])
#print(person['pets']['cat'])


for key in person["children"]:
    print(key)

for key in person['pets']:
    print(person['pets'][key])

#or
#for key in person['pets'].values():
    #print()