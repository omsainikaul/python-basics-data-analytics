a = "Om is good"      #in read mode string/variable is not important to assign

file = open("FILE-HANDLING/robot.txt", "r")     #first we have to create the robot.txt file and "r" means it will be open in read mode
content = file.read()             #.read is used to print the data of the txt file as output
print(content)                    #print the content of the .txt file


file = open("FILE-HANDLING/robot.txt", "r")     #first we have to create the robot.txt file and "r" means it will be open in read mode
content = file.readlines()             #.readlines is used to print the data of the txt file as output as a list of lines
print(content)                    #print the content of the .txt file


file.close()                      #closes the program


#in read mode we have to first create the .txt file which we want to read by the program