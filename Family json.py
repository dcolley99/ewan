import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

for person in fileDataJSON["38DanbyRoad"]:
    print(person)
for person in fileDataJSON["11CheritonClose"]:
    print(person)