# WAP in recursive function to calculate the factorial of the given number.
def fact_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_recursive(n-1)
num=int(input("Enter any number: "))
f = fact_recursive(num)
print("The factorial of a given number is:"+str(f))