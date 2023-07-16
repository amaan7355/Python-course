from re import I


def linearsearch(arr,n,x):
    for i in range(n):
        if (arr[i]==x):
            return i  
    return -1
arr=[3,10,30,45]
n=len(arr)
x=45
result=linearsearch(arr,n,x)
if result != -1:
    print(f"Element is present at index number {result}")
else:
    print("Element is not present in the array")