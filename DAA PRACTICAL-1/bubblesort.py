def bubblesort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
bubblesort(arr)
print("Sorted array:")
print(arr)
