
def bubblesort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                
array=[51, 32, 83, 64, 75, 26]
bubblesort(array)
print(array)
