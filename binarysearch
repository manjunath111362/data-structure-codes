
def binarysearch(arr,num):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            start=mid+1
        else:
            end=mid-1
    return -1
    
array=[11,12,23,34,45,56,67]
num=67
print(binarysearch(array,num))
