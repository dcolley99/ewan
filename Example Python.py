import json

with open('ExampleInformation.json','r') as file:
    fileDataJSON = json.load(file)

personInfo = fileDataJSON["PeopleInfo"]

for person in personInfo:
    peopleList = []
    for key, value in person.items():
        peopleList.append(str(value))
    print(", ".join(peopleList))