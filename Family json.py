import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

danbyRoad = fileDataJSON["38DanbyRoad"]
cheritonClose = fileDataJSON["11CheritonClose"]
UqId = 0
i = 0

for person in danbyRoad:
    peopleList = []
    UqId +=1
    if i == 0:
         peopleList.append(str(UqId))
    for key, value in person.items():
        if isinstance(value, dict) and key == "Height":
            feet = value.get("Feet", 0)
            inches = value.get("Inches", 0)
            peopleList.append(f"{feet}")
            peopleList.append(f"{inches}")
        else:
            peopleList.append(str(value))
    print(", ".join(peopleList))

for member in cheritonClose:
    newList = []
    UqId +=1
    if i == 0:
         newList.append(str(UqId))
    for key, value in member.items():
        if isinstance(value, dict) and key == "Height":
            newList.append(str(value.get("Feet", 0)))
            newList.append(str(value.get("Inches", 0)))
        else:
            newList.append(str(value))
    print(", ".join(newList))
