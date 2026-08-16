names = ["Harry", "Larry", "Perry"]
elements = [1, 34, 67, True, False]

print(names)
#this will print the list(names)

print(type(names))
#this will print the type of the list(names)

print(elements[0])
print(elements[1])
#this will print the elements from the place 0 and 1 from the list(names)

print(len(elements))
#this will print the length of the list(elements)

#list in python are mutable(means we can change the list values)

elements[2] = 69
#this will replace the 67 to 69 in the list(elements)
print(elements)