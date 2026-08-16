items = ["apple", "banana", "orange"]

print(len(items))
#this will print the length of the list(items)

items.append("strawberries")
#this will add strawberries to the last of the list(items) by default
print(items)

items.insert(1, "strawberries")
#this will add strawberries to the 1 position of the list(items)
print(items)

items.extend(["grapes", "pineapples"])
#by this we can add multiple values to the list(items)
print(items)

items.remove("orange")
#by this the banana will be removed from the list(items)
print(items)

print(items.index("banana"))
#this will give first occurence position of the named value(banana) from the list(items)

print(items.count("banana"))
#this will give the number of time the value(banana) occured in the list(items)

items.pop()
#removes the last value from the list(items)
print(items)

items.pop(2)
#removes the value from position 1 of the list(items)
print(items)

items.clear()
#this will clear the whole list(items)
print(items)