try:
    x = int(input("enter a number :"))
    y = 10/x

except ValueError:
    print("please enter a valid number")

except ZeroDivisionError:
    print("division by zero is not allowed")

finally:
    print("i will always run")