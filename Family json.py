import json

with open('FamilyInformation.json', 'r') as file:
    fileContent = file.read()
    fileDataJSON = json.loads(fileContent)

for person in fileDataJSON["38DanbyRoad"]:
    print(person['FirstName'])
