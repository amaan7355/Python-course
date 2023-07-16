def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y,x%y)
n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
print("The GCD of two numbers is:", gcd(n,m))