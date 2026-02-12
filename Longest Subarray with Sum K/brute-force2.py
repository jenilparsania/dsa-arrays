def LongestSubArray(nums:list,target:int)->int:

    n = len(nums)
    length = 0
    for i in range(0,n):
        add = 0
        
        for j in range(i,n):
            add += nums[j]
            if add == target:
                length = max(length,j-i+1)
                
   
    return length
    pass

arr = [-5, 8, -14, 2, 4, 12]
k = -5
print(LongestSubArray(arr,k))