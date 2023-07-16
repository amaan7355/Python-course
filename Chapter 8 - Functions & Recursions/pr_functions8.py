# WAP to convert inches to cms using functions.
def inch(cms):
    return cms*2.54
l=int(input("Enter the length in inches: "))
c=inch(l)
print("Length in centimetres: "+str(c))