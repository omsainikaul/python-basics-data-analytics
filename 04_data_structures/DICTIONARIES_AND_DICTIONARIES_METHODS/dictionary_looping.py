student = {
    "name" : "Om Saini",
    "age" : "18",
    "course" : "B.tech"
}

#Loop through Keys

for key in student :
    print (key)

#prints the key values from the dictionary(student)

#Loop through Values

for value in student.values() :
    print(value)

#prints the values from the dictionary(student)

#Loop through Key Value Pairs

for key, value in student.items() :
    print(key, ":", value)

#prints both the keys and values from the dictionary(student)