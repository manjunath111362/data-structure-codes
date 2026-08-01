def selectionsort(nums):
    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
n = int(input("Enter the number of elements: "))
nums = []
print("Enter the elements:")
for i in range(n):
    nums.append(int(input()))
selectionsort(nums)
print("Sorted array:")
print(nums)
