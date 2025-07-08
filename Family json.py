import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

danbyRoad = fileDataJSON["38DanbyRoad"]
cheritonClose = fileDataJSON["11CheritonClose"]
UqId = 0
i = 0
HeightUqId = 0
heightList = []
HeightUqId = 0
newHeightTable = []
foot = 4
inch = 0
for i in range(27):
    HeightUqId+=1
    if inch >=12:
        inch-=12
        foot+=1
    heightF = str(foot)
    heightI = str(inch)
    print(HeightUqId,", ", heightF, heightI)
    inch+=1
print("")

for person in danbyRoad:
    peopleList = []
    UqId +=1
    if i == 0:
         peopleList.append(str(UqId))
    for key, value in person.items():
        if isinstance(value, dict) and key == "Height":
            footNew = str(value.get("Feet", 0))
            inchNew = str(value.get("Inches", 0))
            HeightUqId = 0
            newHeightTable = []
            foot = 4
            inch = 0
            for i in range(27):
                HeightUqId+=1
                if inch >=12:
                    inch-=12
                    foot+=1
                heightF = str(foot)
                heightI = str(inch)
                inch+=1
                if footNew == heightF and inchNew == heightI:
                    peopleList.append(str(HeightUqId))
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
            footNew = str(value.get("Feet", 0))
            inchNew = str(value.get("Inches", 0))
            HeightUqId = 0
            newHeightTable = []
            foot = 4
            inch = 0
            for i in range(27):
                HeightUqId+=1
                if inch >=12:
                    inch-=12
                    foot+=1
                heightF = str(foot)
                heightI = str(inch)
                inch+=1
                if footNew == heightF and inchNew == heightI:
                    newList.append(str(HeightUqId))
        else:
            newList.append(str(value))
    print(", ".join(newList))
print("")

file.close()