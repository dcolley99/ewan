import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

familyTable = []
for person in fileDataJSON["38DanbyRoad"]:
    familyTable.append([person["FirstName"], person["LastName"], person["Age"], (person["Height"]["Feet"], person["Height"]["Inches"]), person["HairColour"]])
    familyTable.append("\n")

print(familyTable)

#for person in fileDataJSON["38DanbyRoad"]:
#    print(person)
#for person in fileDataJSON["11CheritonClose"]:
#    print(person)