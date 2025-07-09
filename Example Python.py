import json

# Load JSON file
with open('ExampleInformation.json', 'r') as file:
    fileDataJSON = json.load(file)

smallFamily = fileDataJSON["PeopleInfo"]

print("Information (Level 1 (Name/Age/Occupation))")
for person in smallFamily:
    peopleList = []
    for key, value in person.items():
        if not isinstance(value, dict):
            peopleList.append(f"{value}")
    print(", ".join(peopleList))
print("")

print("Information (Level 2 (Town, cm/inches)): ")
for person in smallFamily:
    for key, value in person.items():
        if isinstance(value, dict):
            infoList = []
            for sub_key, sub_value in value.items():
                if not isinstance(sub_value, dict):
                    infoList.append(f"{sub_value}")
            print(", ".join(infoList))
print("")

print("Information (Level 3 (Country/Continent)): ")
for person in smallFamily:
    for key, value in person.items():
        if isinstance(value, dict):
            for subkey, sub_value in value.items():
                if isinstance(sub_value, dict):
                    locationList = []
                    for subKey, subValue in sub_value.items():
                        locationList.append(f"{subValue}")
                    print(", ".join(locationList))
file.close()