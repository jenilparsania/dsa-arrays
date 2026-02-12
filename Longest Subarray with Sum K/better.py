def longestSubarray(a:list,k:int)->int:

    sum_map = dict()
    add = 0
    max_length = 0
    for i in range(0,len(a)):
        add += a[i]
        if add == k:
            max_length = i+1
        
        rem = add - k
        if rem in sum_map:
            l = i - sum_map[rem]
            max_length = max(max_length,l)

        if add not in sum_map:
            sum_map[add] = i
        
    return max_length
    

arr = [-5, 8, -14, 2, 4, 12]
k = -5
print(longestSubarray(arr,k))