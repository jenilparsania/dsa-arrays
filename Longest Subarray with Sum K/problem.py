"""  
Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
"""

def LongestSubArray(nums:list,target:int)->int:

    n = len(nums)
    add = 0
    ans = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if add < target:
                add += nums[i] + nums[j]
            elif add == target:
                ans = max(ans,j-i+1)
            elif add > target:
                add = 0
                break

    return ans
    pass

arr = [-5, 8, -14, 2, 4, 12]
k = -5
print(LongestSubArray(arr,k))
