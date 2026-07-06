Name = input("Enter a Name :")
Father_Name = input("Enter a Father Name :")
Age = int(input("Enter a Age :"))
Marks = int(input("Enter a Marks :"))
print("========== Student Card ==========")
print("Student Name : ",Name)
print("Father Name  :",Father_Name)
print("Age          :",Age)
print("Marks        :",Marks)
#Grade
if(Marks>=90 and Marks<=100):
    Grade=(" A+")
elif(Marks>=80 and Marks <= 89):
    Grade=(" A")
elif(Marks>=70 and Marks <= 79):
    Grade=("B")
elif(Marks>=60 and Marks <= 69):
    Grade=("c")
elif(Marks>=101 ):
   Grade=("Enter a wrong marks")
else:
    Grade=("Grade = Fail")
print("Grade        :",Grade)
#Status 
if(Marks>=60 and Marks<=100):
    status=("Pass")
else:
    status=("Fail")
print("Status       :",status)

print("==================================")