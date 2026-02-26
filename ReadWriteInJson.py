# import json

# with open("JsonFile.json", "r") as file:
#     print(json.dumps(data, indent=4))

# print(data)

import json

with open("JsonFile.json", "r") as file:
    data = json.load(file)

print(json.dumps(data, indent=4))