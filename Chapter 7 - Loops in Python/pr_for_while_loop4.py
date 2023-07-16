# WAP to find the sum of first n natural numbers using while loop.
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)