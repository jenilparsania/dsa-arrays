# basic idea : as the total goes to negative, change it to 0 and move forward  

def KadaneAlgo(nums:list):
    n = len(nums)
    maxi = float("-inf")
    total = 0
    i = 0 
    for i in range(n):
        total += nums[i]
        maxi = max(maxi,total)

        if total<0:
            total = 0
        
    return maxi
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(KadaneAlgo(nums))