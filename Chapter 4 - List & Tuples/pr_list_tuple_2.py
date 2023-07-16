# WAP to accept marks of 6 students and display them in a sorted manner.
m1=int(input("Enter the marks of first student: "))
m2=int(input("Enter the marks of second student: "))
m3=int(input("Enter the marks of third student: "))
m4=int(input("Enter the marks of fouth student: "))
m5=int(input("Enter the marks of fifth student: "))
m6=int(input("Enter the marks of sixth student: "))
list=[m1,m2,m3,m4,m5,m6]
list.sort()
print(list)