# WAP using function to find the greatest of three numbers.
def greatest(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
m=greatest(n1, n2, n3)
print(m)