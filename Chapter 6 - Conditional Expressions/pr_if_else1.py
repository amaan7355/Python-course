# WAP to find greatest of four numbers entered by the user.
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
num4=int(input("Enter number 4: "))
if (num1>num2):
    f1=num1
else:
    f1=num2
if (num3>num4):
    f2=num3
else:
    f2=num4
if (f1>f2):
    print("Greatest number is:",f1)
else:
    print("Greatest number is:",f2)