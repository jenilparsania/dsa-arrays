"""You are given an array 'a' of 'n' integers.



A majority element in the array ‘a’ is an element that appears more than 'n' / 2 times.

Find the majority element of the array.



It is guaranteed that the array 'a' always has a majority element.



Example:
Input: ‘n’ = 9, ‘a’ = [2, 2, 1, 3, 1, 1, 3, 1, 1]
"""

def MajorityElement(a):
    n = len(a)
    for i in range(n):
        count = 0
        for j in range(n):
            if a[j] == a[i]:
                count+=1
        
        if count > n//2:
            return a[j]
    pass

a = [2, 2, 1, 3, 1, 1, 3, 1, 1]
print(MajorityElement(a))