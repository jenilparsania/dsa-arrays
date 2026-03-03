"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
"""


def LongestConsSeq(nums):
    max_count = 0
    n=len(nums)
    for i in range(n):
        a = nums[i]
        count=1
        while(a+1 in nums):
            count+=1
            a = a+1
        max_count = max(count,max_count)
    
    return max_count


    pass

nums = [1,99,101,98,2,5,3,100,1]

print(LongestConsSeq(nums))