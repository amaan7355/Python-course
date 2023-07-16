def swap(x,y):
    x,y=y,x
    return x,y
n1=int(input("Enter first no.: "))
n2=int(input("Enter second no.: "))
print(f"value of x before swapping= {n1} & value of y before swapping= {n2}")
b,s=swap(n1,n2)
print(f"value of x after swapping= {b} & value of y after swapping= {s}")