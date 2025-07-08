import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)
keyList = ["'FirstName'","'LastName'","'Age'","'Height'","'HairColour'"]
filterTable = fileDataJSON["38DanbyRoad"]

for i in filterTable:
    valuesList = []
    items = i.values()
    for j in items: 
        newList = valuesList.append(j)
        print(j)
    print(str(newList).strip("None"))

#for person in fileDataJSON["38DanbyRoad"]:
#    print(person)
#for person in fileDataJSON["11CheritonClose"]:
#    print(person)
