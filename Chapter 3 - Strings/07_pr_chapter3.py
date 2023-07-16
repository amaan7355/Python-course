# WAP to convert a string into new string in which first and last characters got interchanged from the input string.
str='amaan'
newstr=' '
s1=str[0]
s2=str[len(str)-1]
s3=str[1:len(str)-1]
print(s2+s3+s1)