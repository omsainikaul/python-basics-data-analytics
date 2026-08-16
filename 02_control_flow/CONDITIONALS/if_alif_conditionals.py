marks = int(input("Enter marks :"))

if marks >= 80:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Grade C")

if marks % 2 == 0:
    print("Marks is even!")

else:
    print("Marks is odd")