# TC-> O(NlogN + N)
# SC-> O(1)
#  the solution is of sorting the array and then checking for longest sequence
def LongestConsSeq(nums:list):
    nums.sort()    # O(NlogN)
    last_smaller = float("-inf")
    count=1
    longest = 0
    n = len(nums)
    for i in range(0,n):   #O(N)
        if nums[i] - last_smaller > 1:
            last_smaller = nums[i]
            count=1
        elif nums[i]-last_smaller ==1:
            count+=1
            last_smaller = nums[i]
        
        longest = max(count,longest)
        
    return longest



    pass

nums = [1,99,101,98,2,5,3,100,1]

print(LongestConsSeq(nums))  