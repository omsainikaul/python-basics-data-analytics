print("Initiallizinggg...")

a = int(input("enter value of a : "))
b = int(input("enter value of b : "))

try:                                           #first the code will try that it will run or not
    print("the value of a/b is : ", a/b)       #if we input value of b = 0 then there will be error

except Exception as e:                         #so for error there is try and except function
    print("Some error occured! -", e)          #the Exception as e tells due to which the error occurs

print("Thank You...")