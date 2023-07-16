# WAP to print first n lines of the following pattern.
'''
* * *
* *                            for n=3
*
'''
#def pattern(n):
n=3
for i in range(n):
    print("*" * (n-i))
#pattern(3)