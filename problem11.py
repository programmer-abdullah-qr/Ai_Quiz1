#level 3
Marks = int (input("Enter a Marks:"))
if(Marks>=90 and Marks<=100):
    print("Grade = A+")
elif(Marks>=80 and Marks <= 89):
    print("Grade = A")
elif(Marks>=70 and Marks <= 79):
    print("Grade = B")
elif(Marks>=60 and Marks <= 69):
    print("Grade = c")
elif(Marks>=101 ):
    print("Enter a wrong marks")
else:
    print("Grade = Fail")
