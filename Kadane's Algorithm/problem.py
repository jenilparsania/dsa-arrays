"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
"""
# TC -> O(N(N+1)/2) approx equals to O(N^2)
def maxSum(nums:list):
    n = len(nums)
    maxi = float("-inf") # very important, not to take this as 0, because an array may have all the negative elements in it.
    total = 0
    i = 0 
    j = 0
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[j]
            maxi = max(maxi,total)
        
    return maxi
    pass

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum(nums))
