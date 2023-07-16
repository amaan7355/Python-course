# WAP to enter a number by a user and print the factorial of it using for loop.
n=int(input("Enter a number: "))
f=1
for i in range (1,n+1):
    f=f*i 
print("The factorial of a given number is",f)