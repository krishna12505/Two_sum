def twosum(nums,target):
    l = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                l.append(nums[i])
                l.append(nums[j])
    return l

nums = [2,4,6,3]
target = 9
result = twosum(nums, target)
print(result)