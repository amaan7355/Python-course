from re import I


#WAP to print multiplication table of a number entered by a user using for loop.
n=int(input("Enter the number: "))
for i in range (1,11):
    #c=n*i 
    print(f"{n}X{i}={n*i}")
    #print(str(n)+"X"+str(i)+"="+str(i*n))