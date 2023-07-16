# WAP in recursive function to calculate the sum of first n natural number enter by the user.
def sum_recursive(n):
        if n == 1:
                return 1
        else:
                return sum_recursive(n-1) + n
num=int(input("Enter any number: "))
s=sum_recursive(num)
print("The sum of first n natural number is: "+str(s))