a = "\n Yashant is also good"

file = open("FILE-HANDLING/robot.txt", "a")  #"a" append mode adds the values at the end of the txt files
file.write(a)

file.close()