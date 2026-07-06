num1 = int(input("Enter a First Digit:"))
num2 = int(input("Enter a Second Digit:"))
num3 = int(input("Enter a Third Digit:"))
if(num1>=num2 and num1>=num3):
    print("First is the largest number:",num1)
elif(num2>=num3):
    print("Second is the largest number :",num2)
else:
    print("Third is the largest number:",num3)