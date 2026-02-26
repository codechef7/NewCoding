#type1....................
# import json

# with open("JsonFile.json", "r") as file:
#     print(json.dumps(data, indent=4))

# print(data)

#type2.........................
# import json

# with open("JsonFile.json", "r") as file:
#     data = json.load(file)

# print(json.dumps(data, indent=4))

#type3....................

# import json

# with open("JsonFile.json","r") as file:
#     data=json.load(file)

# for student in data:
#     print("ID:",student["id"])
#     print("Name:",student["name"])
#     print("Age:",student["age"])
#     print("Course:",student["course"])
#     print("City:",student["city"])
#     print(".............................")


#to add more students 
import json

with open("JsonFile.json", "r") as file:
    data=json.load(file)

new_student1={
    "id": 108,
    "name": "Abhinav Mishra",
    "age": 22,
    "course": "BTech",
    "city": "Bhopal"
}

new_student2={
    "id": 109,
    "name": "Atharva Kailash Sahu",
    "age": 22,
    "course": "BTech",
    "city": "Chhindwara"
}

data.append(new_student1)
data.append(new_student2)

with open("JsonFile.json","w") as file:
    json.dump(data, file, indent=4)

for students in data:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("City:", student["city"])
    print("----------------------")
    
