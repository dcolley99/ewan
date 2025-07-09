import json

with open('ExampleInformation.json','r') as file:
    fileDataJSON = json.load(file)

UqId = 0
heightUqId = 0
personInfo = fileDataJSON["PeopleInfo"]
sub_sub_key = ""

print("Information (Dictionaries): ")
for person in personInfo:
    dictList = []
    heightUqId+=1
    dictList.append(str(heightUqId))
    for key, value in person.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    for subKey, subValue in sub_value.items():
                        dictList.append(str(subValue))
                else:
                    dictList.append(str(sub_value))
    print(", ".join(dictList))
print("")

print("Information (People): ")
for person in personInfo:
    peopleList = []
    UqId+=1
    peopleList.append(str(UqId))
    for key, value in person.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    for subKey, subValue in sub_value.items():
                        dictList.append(str(subValue))
                else:
                    dictList.append(str(sub_value))
        else:
            peopleList.append(str(value))
    print(", ".join(peopleList))
file.close()