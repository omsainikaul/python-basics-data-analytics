student = {
    "name" : "Om Saini",
    "city" : "Meerut",
    "company" : "Amazon"
}

print(student.get("nameee"))
#does not give error for spelling or wrong input command

print(student.keys())
#prints the keys of the dictionary

print(student.values())
#prints the values of the dictionary

print(student.items())
#prints all the items of the dictionary means both the key and values

student["city"] = "Gurugram"
#update city value Meerut ---> Gurugram
print(student)

student.pop("name")
#removes name key from the dictionary
print(student)

student["class"] = "12th"
#adds new value in the dictionary
print(student)

student.popitem()
#removes latest added key from the dictionary
print(student)

del student["city"]
#deletes the city key from the dictionary
print(student)

student.clear()
#clears the whole dictionary
print(student)