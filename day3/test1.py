input = [1,2,3,4, 5, 6]


output1 = list(map(lambda x: x**2, input))
print(output1)

output2 = list(filter(lambda x: x%2!=0, output1))

print(output2)