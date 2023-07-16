# WAP using function to convert celcius to fahrenheit.
def far(cel):
    temp=(cel * (9/5) + 32)
    return temp
c=int(input("Enter the temperature in celcius: "))
f=far(c)
print("Temperature in fahrenheit is:"+str(f))