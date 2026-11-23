def binarysearch(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1
n = int(input("Enter number of elements: "))
arr = []
print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter the element to search: "))
result = binarysearch(arr,target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
