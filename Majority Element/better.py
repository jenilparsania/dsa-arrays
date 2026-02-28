def MajorityElement(nums:list):
    my_dict = dict()
    n = len(nums)

    for i in range(n):
        my_dict[nums[i]] = my_dict.get(nums[i],0) + 1
    
    for k,v in my_dict.items():
        if v > n//2:
            return k
    pass


a = [2, 2, 1, 3, 1, 1, 3, 1, 1]
print(MajorityElement(a))