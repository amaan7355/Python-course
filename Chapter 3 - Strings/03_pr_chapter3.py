# WAP to detect double spaces in a string and replace double spaces from single space.
c=0
s="Hello  My name is Amaan Alam."
doubleSpaces=s.find("  ")
print(doubleSpaces)
str=s.replace("  "," ")
print(str)
