def MajorityElement(nums):
    result = []
    maxi = float("-inf")
    n = len(nums)
    for i in range(n-1,-1,-1):
        e = max(maxi,nums[i])
        if e > maxi:
            result.append(e)
            maxi=e

    result.reverse()
    return result
    pass

a = [1, 2, 3, 2]
print(MajorityElement(a))

"""
TC -> O(2N)
SC -> O(N)
"""

