def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[ x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
print("Original Array:", arr)
sorted_arr = quicksort(arr)
print("Sorted Array:", sorted_arr)
