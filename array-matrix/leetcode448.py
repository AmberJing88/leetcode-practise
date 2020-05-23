from collections import defaultdict

def find_missing(nums):

    for j in range(len(nums)):
        if nums[j] != nums[nums[j] -1]:
            nums[j], nums[nums[j] -1] = nums[nums[j]-1], nums[j]
            
    result = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            result.append(i+1)

    return result

print(find_missing([4,3,2,7,8,2,3,1]))
