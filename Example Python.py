#IMPORTANT
#Make a detection system for matching the UQID to each line number in the text document. Use ChatGPT, Internet, etc.

import json

filename = input("Enter file name... ")
with open(filename, 'r') as file:
    fileDataJSON = json.load(file)

uqid_counter = 1
structured_output = []

def assign_uqid():
    global uqid_counter
    uqid = uqid_counter
    uqid_counter += 1
    return uqid

def flatten(obj, top_level_uqid, level):
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_uqid = assign_uqid()
            structured_output.append({
                "UqID": key_uqid,
                "PUqID": top_level_uqid,
                "Type": "Key",
                "Level": level,
                "Value": key
            })
            flatten(value, top_level_uqid, level + 1)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            index_uqid = assign_uqid()
            structured_output.append({
                "UqID": index_uqid,
                "PUqID": top_level_uqid,
                "Type": "Key",
                "Level": level,
                "Value": f"[{i}]"
            })
            flatten(item, top_level_uqid, level + 1)
    else:
        value_uqid = assign_uqid()
        structured_output.append({
            "UqID": value_uqid,
            "PUqID": top_level_uqid,
            "Type": "Value",
            "Level": level,
            "Value": str(obj)
        })

def iterate_top(obj):
    if isinstance(obj, dict):
        return obj.items()
    elif isinstance(obj, list):
        return enumerate(obj)
    else:
        return []

for top_key, people in iterate_top(fileDataJSON):
    top_uqid = assign_uqid()
    structured_output.append({
        "UqID": top_uqid,
        "PUqID": 0,
        "Type": "Key",
        "Level": 1,
        "Value": top_key
    })
    if isinstance(people, (list, dict)):
        if isinstance(people, list):
            for person in people:
                flatten(person, top_uqid, level=2)
        else:
            flatten(people, top_uqid, level=2)
    else:
        flatten(people, top_uqid, level=2)

print(f"{'UqID':<6} {'PUqID':<6} {'Level':<5} {'Type':<6} Value")
for entry in structured_output:
    print(f"{entry['UqID']:<6} {entry['PUqID']:<6} {entry['Level']:<5} {entry['Type']:<6} {entry['Value']}")
