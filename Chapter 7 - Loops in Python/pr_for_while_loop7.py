# WAP to print the following star pattern.
'''
*  *  *
*     *
*  *  *
'''
n=3
for i in range(n):
    if i == 0:
        print("*"*(n-i-2), end="")
        print(" "*(n-i-1), end="")
        print("*"*(n-i-2), end="")
        print(" "*(n-i-1), end="")
        print("*"*(n-i-2))
    elif i % 2 != 0:
        print("*"*(n-i-1), end="")
        print(" "*(2*n-1), end="")
        print("*"*(n-i-1))
    elif i % 2 == 0:
        print("*"*(n-i), end="")
        print(" "*(2*n-4), end="")
        print("*"*(n-i), end="")
        print(" "*(2*n-4), end="")
        print("*"*(n-i))