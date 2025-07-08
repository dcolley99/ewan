import json

with open('FamilyInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

danbyRoad = fileDataJSON["38DanbyRoad"]
cheritonClose = fileDataJSON["11CheritonClose"]
UqId = 0
i = 0
HeightUqId = 0
heightList = []

def HeightUnique(uniqueID):
    foot1=4
    inch1=0
    j=0
    for i in range(24):
        heightList = []
        j+=1
        if j==uniqueID:
            heightList.append(j)
            #When back from lunch, investigate error with printing ALL heights.
            return
        inch1+=1
        if inch1 >=13:
            inch1==0
            foot1+=1


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
print("")

for height in danbyRoad:
    HeightUqId+=1
    if i == 0:
        heightList.append(str(HeightUqId))
    for key, value in height.items():
        if isinstance(value, dict) and key == "Height":
            heightList.append(str(value.get("Feet", 0)))
            heightList.append(str(value.get("Inches", 0)))
    print(", ".join(heightList))

for height in cheritonClose:
    HeightUqId+=1
    if i == 0:
        heightList.append(str(HeightUqId))
    for key, value in height.items():
        if isinstance(value, dict) and key == "Height":
            heightList.append(str(value.get("Feet", 0)))
            heightList.append(str(value.get("Inches", 0)))
    print(", ".join(heightList))

HeightUnique(UqId)