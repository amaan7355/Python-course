# WAP to print only those words in a string whose element count is greater than or equal to 4 words.
s=("Hello! my name is Amaan Alam")
s=s.split()
for word in s:
    if len(word)>4:
        print(word)