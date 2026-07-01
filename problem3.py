Age = int (input("Enter a age :"))
if(Age<18):
    print("you age is minor: ",Age)
elif(Age>=18 and Age<59):
    print("Your Adult")
else:
    print("Your are Senior Citizen")