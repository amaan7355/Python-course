def eratosthenes(n):
    prime_list=[]
    for i in range(2,n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i,n+1,i):
                prime_list.append(j)
num=int(input("Enter the number: "))
eratosthenes(num)