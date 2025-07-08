import json

with open('ExampleInformation.json','r') as file:
    fileDataJSON = json.load(file)

UqId = 0
heightUqId = 0
personInfo = fileDataJSON["PeopleInfo"]

for person in personInfo:
    heightList = []
    heightUqId+=1
    for key, value in person.items():
        if isinstance(value, dict) and key == "height":
            cmNew = str(value.get("cm"))
            inchesNew = str(value.get("inches"))
            heightList.append(str(heightUqId))
            heightList.append(":")
            heightList.append(cmNew)
            heightList.append(inchesNew)
    print(" ".join(heightList))
print("")

for person in personInfo:
    peopleList = []
    UqId+=1
    peopleList.append(str(UqId))
    for key, value in person.items():
        if isinstance(value, dict) and key == "height":
            cmNew = str(value.get("cm"))
            inchesNew = str(value.get("inches"))
            peopleList.append(cmNew)
            peopleList.append(inchesNew)
        else:
            peopleList.append(str(value))
    print(", ".join(peopleList))