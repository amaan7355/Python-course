# A spam comment is defined as a text containing following keywords:["make a lot of money","buy now","subscribe this",] WAP to detect these spams.
text=input("Enter the text: ")
if ("make a lot of money" in text):
    spam = True
elif('buy now' in text):
    spam = True
elif('subscribe this' in text):
    spam = True
else:
    spam = False
if(spam):
    print("This text is spam.")
else:
    print("This text is not spam")