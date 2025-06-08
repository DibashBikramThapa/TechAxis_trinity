a = [1, 2, 3, 4, 5, 6, 7, 8 ,10]

my_output = list(filter(lambda x: x%2==0, a))

my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c', 2))

my_dict.update({'a':2})
my_dict['a'] = 3

print(my_dict)

list_comp = [1, 2, 3, 4]
# a = []
# for each in list_comp:
#     if each%2==0:
#         a.append(each)
a = [each if each%2==0 else False for each in list_comp ]
print(a)


