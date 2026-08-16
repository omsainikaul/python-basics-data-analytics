name = "Om Saini  "

# name[0] = "A" 
#This is not allowed as this will not replace O with A, it will give an error

print(name)

print(len(name)) #This will print the name length

print(name.lower()) #This will print the name in Lower Case

print(name.upper()) #This will print the name in Upper Case

print(name.strip()) #This will remove the space from the last of the name

print(name.replace("Saini", "Saini Sahab")) #This will replace the text or the words

print(name.isalpha()) #True if there are only characters no numbers
                      #Output is False because there is space between the words

print(name.isnumeric()) #True if there are only numbers no characters