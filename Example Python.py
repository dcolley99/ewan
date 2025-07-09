import json

with open('ExampleInformation.json','r') as file:
    fileDataJSON = json.load(file)

UqId = 0
heightUqId = 0
personInfo = fileDataJSON["PeopleInfo"]
sub_sub_key = ""

print("Information (Dictionaries): ")
for person in personInfo:
    heightList = []
    heightUqId+=1
    for key, value in person.items():
        if isinstance(value, dict):
            heightList.append(str(heightUqId))
            heightList.append(":")
            for sub_key, sub_value in value.items():
                heightList.append(str(sub_value))
    print(" ".join(heightList))
print("")

print("Information (People): ")
for person in personInfo:
    peopleList = []
    UqId+=1
    peopleList.append(str(UqId))
    for key, value in person.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                peopleList.append(str(sub_value))
        else:
            peopleList.append(str(value))
    print(", ".join(peopleList))
file.close()