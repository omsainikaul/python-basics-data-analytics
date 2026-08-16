student = {
    "name" : "Om Saini",
    "age" : "18",
    "course" : "B.tech"
}

print("name" in student)
#Returns True if the key named as "name" exist in the dictionary(student)

new_student = student.copy()
#creates a copy of the dictionary
print(new_student)

student.update({
    "course" : "python",
    "level" : "beginner"
})
#updates the values in the dictionary(student)
print(student)