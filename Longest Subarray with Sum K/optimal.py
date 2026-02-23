def longestSubArrayWithSumK(a:list,k:int)->int:
    # this example shows great use of two pointers
    # this optimal solution is still having some errors
    
    n = len(a)
    left = 0
    right = 0
    add = a[0]
    max_lenght = 0
    while right<n:
        while left <= right and add > k:
            add -= a[left]
            left+=1
        if add == k:
            max_lenght = max(max_lenght,right-left+1)
        
        right+=1
        if right<n:
            add += a[right]
        
    
    return max_lenght


    pass

arr = [-5, 8, -14, 2, 4, 12]
k = -5
print(longestSubArrayWithSumK(arr,k))