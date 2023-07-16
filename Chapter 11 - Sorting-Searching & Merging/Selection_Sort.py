def selectionsort(list):
    for i in range(len(list)-1,0,-1):
        max=0
        for location in range(1,i+1):
            if list[location]>list[max]:
                max=location
        temp=list[i]
        list[i]=list[max]
        list[max]=temp
list=[14,46,43,27,57,41,45,21,70]
selectionsort(list)
print(list)