import json

records = [
    {'name': "John", "age": 23, "location": "kamaladi"},
    {'name': "John", "age": 23, "location": "kamaladi"},
    {'name': "John", "age": 23, "location": "kamaladi"},
    {'name': "Ram", "age": 23, "location": "kamaladi"},
    {'name': "Shyam", "age": 23, "location": "kamaladi"},
    {'name': "Shyam1", "age": 23, "location": "kamaladi"},
]
file_loc = "my.json"
json_rec = []
# Open the JSON file and load its content
with open(file_loc, 'r') as file:
    try:
        json_rec = json.load(file)
    except Exception as e:
        print(f'error when reading json file: {e}')

with open(file_loc, 'w+') as file:
    to_write = []
    for each in records:
        # to handle duplicate name
        if each['name'] not in map(lambda x: x['name'], json_rec):
            to_write.append(each)
    # join two list
    to_write.extend(json_rec)
    print('to write:', to_write)
    # sort list of dict using key name in dict
    sorted_list = sorted(to_write, key=lambda x : x['name'])
    # dump json and write the file
    file.write(json.dumps(sorted_list))
