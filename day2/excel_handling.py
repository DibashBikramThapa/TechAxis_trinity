import pandas as pd

records = [
    {'name': "John", "age": 23, "location": "kamaladi"},
    {'name': "Ram", "age": 23, "location": "kamaladi"},
    {'name': "Sita", "age": 23, "location": "kamaladi"},
    {'name': "Shyam", "age": 23, "location": "kamaladi"},
]
file_path = 'record.xlsx'

try:
    df = pd.read_excel(file_path)
    df_records = df.to_dict(orient='records')
except Exception as e:
    print('error1', e)
    df_records = []

to_add_rec = [each for each in records if each['name'] not in map(lambda x: x['name'], df_records)]
print(to_add_rec)
if to_add_rec:
    final_rec = df_records + to_add_rec
    print("🚀 ~ final_rec:", final_rec)
    df = pd.DataFrame(final_rec)
    df.to_excel(file_path, index=False)

# records = [("John", 23, "kamaladi"),
#            ("John", 23, "kamaladi"),
#            ("John", 23, "kamaladi")
#         ]
# df = pd.DataFrame(records, columns=['name', 'age', 'location'])
# df.to_excel('record1.xlsx', index=False)
# df.to_csv('record.csv', index=False)




