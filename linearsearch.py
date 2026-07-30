def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1 
    
numbers = [12, 45, 7, 23, 89, 34]
print(linear_search(numbers, 23))
