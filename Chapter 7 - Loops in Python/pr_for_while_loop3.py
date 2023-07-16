# WAP to print multiplication table of a number entered by a user using while loop.
n=int(input("Enter the number: "))
i=1
while i<=10:
    #print(i*n)
    print(f"{n}X{i}={n*i}")
    #print(str(n)+"X"+str(i)+"="+str(i*n))
    i=i+1