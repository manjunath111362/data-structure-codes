def selectionsort(nums):

    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
                
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [51, 32, 83, 64, 75, 26]
selectionsort(nums)

print(nums)
