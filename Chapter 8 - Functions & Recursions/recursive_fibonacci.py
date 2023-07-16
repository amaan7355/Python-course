def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

terms=int(input("Enter the range of series: "))
if terms <= 0:
    print("Please Enter a positive integer.")
else:
    print("Fibonacci series: ")
    for i in range(terms):
        print(recur_fibo(i))