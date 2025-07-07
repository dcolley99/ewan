import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

for person in fileDataJSON["38DanbyRoad"]:
    print(person['FirstName'])
