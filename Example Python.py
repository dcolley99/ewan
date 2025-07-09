import json

filename = input("Enter file name... ")
with open(filename, 'r') as file:
    fileDataJSON = json.load(file)

level_list = []
max_level = 1

def collect_by_level(obj, level=1, results=None):
    if results is None:
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

root_items = []

if isinstance(fileDataJSON, dict):
    if all(isinstance(v, list) for v in fileDataJSON.values()):
        for sublist in fileDataJSON.values():
            root_items.extend(sublist)
    else:
        root_items = [fileDataJSON]

elif isinstance(fileDataJSON, list):
    root_items = fileDataJSON

else:
    raise TypeError("Unsupported JSON root format")

for item in root_items:
    values_by_level = collect_by_level(item, level=1)
    level_list.append(values_by_level)
    max_level = max(max_level, max((k for k in values_by_level if isinstance(k, int)), default=1))

for level in range(2, max_level + 1):
    lines = [
        ", ".join(str(v) for v in levels[level])
        for levels in level_list if level in levels
    ]
    if lines:
        print(f"Information (Level {level - 1}):")
        for line in lines:
            print(line)
        print("")

file.close()