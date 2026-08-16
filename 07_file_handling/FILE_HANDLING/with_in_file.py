a = "\n Om is good"

with open("FILE-HANDLING/robot.txt", "a") as file:      #with makes the code simple and easy, there can be any mode like "w", "r", "a"
    file.write(a)                                       #no need to use file.close() as with automatically does it