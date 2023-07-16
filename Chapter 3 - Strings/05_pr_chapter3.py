# WAP to print even length woeds in a string.
s= "I am amaan alam"
s=s.split()
for word in s:
    if len(word)%2==0:
        print(word)
