#python dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

car1 = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2018
}

car2 = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2020
}

car3 = {
  "brand": "BMW",
  "model": "X5",
  "year": 2022
}

print(car2)

#access list items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#change values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#add items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#remove items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)