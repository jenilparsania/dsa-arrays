def TwoSum(nums:list,target):
    hash_map = dict()
    for i in range(0,len(nums)):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]] = i 

    pass

nums = [2,7,11,15]
target = 17

print(TwoSum(nums,target))