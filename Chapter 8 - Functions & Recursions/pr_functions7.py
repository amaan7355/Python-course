# WAP to print multiplication table of a number enter by the user using functions.
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
c=int(input("Enter any number: "))
table(c)