import json

filename = str(input("Enter file name... "))
with open(filename, 'r') as file:
    fileDataJSON = json.load(file)

level_list = []
max_level = 1

def collect_by_level(obj, level=1, results=None):
    if results == None:
        results = {}

    if isinstance(obj, dict):
        for v in obj.values():
            collect_by_level(v, level + 1, results)
    elif isinstance(obj, list):
        for item in obj:
            collect_by_level(item, level, results)
    else:
        if level not in results:
            results[level] = []
        results[level].append(str(obj))
    
    return results


for key, value in fileDataJSON.items():
    jsonScript = value

for person in jsonScript:
    values_by_level = collect_by_level(person, level=1)
    level_list.append(values_by_level)
    max_level = max(max_level, max(values_by_level.keys()))

for level in range(2, max_level+1):
    print(f"Information (Level {level-1}):")
    for levels in level_list:
        if level in levels:
            print(", ".join(levels[level]))
    print("")
file.close()