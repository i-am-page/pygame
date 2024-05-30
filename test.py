def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if i != len(nums) and nums[i] != nums[i - 1]:
            nums[j] = nums[i - 1]
            nums[j+1] = nums[i]
            j += 1
    return nums,j+1


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
