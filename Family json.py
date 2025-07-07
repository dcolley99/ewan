import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)
keyList = ["FirstName","LastName","Age","Height","HairColour"]
familyTable = []
filterTable = fileDataJSON["38DanbyRoad"]
i=0
for person in filterTable:
    familyTable.append(filterTable[i])
    familyTable.append("\n")
    i+=1
    printable = filterTable[0]
    #Fix it jumping from one object and key. Should only jump one key.
print(familyTable)

#for person in fileDataJSON["38DanbyRoad"]:
#    print(person)
#for person in fileDataJSON["11CheritonClose"]:
#    print(person)
