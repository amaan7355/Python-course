def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for idx in range(i):
            if list[idx]>list[idx+1]:
                temp=list[idx]
                list[idx]=list[idx+1]
                list[idx+1]=temp
list=[19,2,31,45,11,121,127]
bubblesort(list)
print(list)