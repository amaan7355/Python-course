# WAP to find whether a given username contains less than 10 characters or not.
username=input("Enter your username: ")
s=len(username)
print("Username contains",+s,"characters")
if (s<=10):
    print("Username entered is under than 10 characters.")
else:
    print("Username entered is above 10 characters.")