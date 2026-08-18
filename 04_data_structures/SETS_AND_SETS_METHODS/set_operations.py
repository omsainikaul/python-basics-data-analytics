a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
#gives output by joining set a and b
#but gives duplicate values only once in the output
print(result)

result = a.intersection(b)
#give only the common values from both sets
print(result)