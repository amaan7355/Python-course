# WAP to enter a number by a user and check whether it is prime or not.
n=int(input("Enter a number: "))
c=0
for i in range (1,n+1):
    if (n%i==0):
        c=c+1
if (c==2):
    print("This is a prime number")
else:
    print("This is not a prime number")
    
'''Same program using while loop!
n=int(input("Enter a number: "))
c=0
i=2
while (i<n):
    if (n%i==0):
        c=c+1
        i=i+1        
if (c==0):
    print("This is a prime number")
else:
    print("This is not a prime number")'''