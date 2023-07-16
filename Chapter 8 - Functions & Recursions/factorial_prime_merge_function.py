def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def chk_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if(c<=2):
        return True
    else:
        return False
yn='y'
while(yn=='y'):
    number=int(input("Enter a no.: "))
    choice=int(input("Enter your choice, press 1 for factorial and 2 for prime no.: "))
    
    if(choice==1):
        r1=fact(number)
        print("Factorial=",r1)

    elif(choice==2):
        r2=chk_prime(number)

        if(r2==True):
            print("prime no.")
        else:
            print("Not a prime no.")
    elif(choice!=1 or choice!=2):

        exit()

    yn=(input("Do you want to continue, \n press y for yes and n for no: "))