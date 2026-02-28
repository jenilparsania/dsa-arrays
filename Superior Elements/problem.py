"""
Problem statement
There is an integer array ‘a’ of size ‘n’.



An element is called a Superior Element if it is greater than all the elements present to its right.



You must return an array all Superior Elements in the array ‘a’.



Note:

The last element of the array is always a Superior Element. 


Example

Input: a = [1, 2, 3, 2], n = 4
"""

def MajorityElement(nums:list):
    n = len(nums)
    answer = []
    flag = True
    for i in range(n):
        flag = True
        for j in range(i+1,n):
            print(f"{a[i]} < {a[j]}")
            
            if a[i] < a[j]:
                flag = False
        
        if flag:
            print(f"{i} => {a[i]} ; {j} => {a[j]}")
            answer.append(a[i])
        
    return answer
    pass

a = [1, 2, 3, 2]
print(MajorityElement(a))
"""
EXPLAINATION FOR HOW THE LAST ELEMENT GETS ADDED BY ITSELF
This loop:

for j in range(i+1, n):

If i is the last index (i = 3), then:

range(4, 4)

This is an empty range, so the inner loop does not execute even once.

But here’s the important part:

Since the inner loop never runs:

flag remains True

So this condition becomes true:

if flag:
    answer.append(a[i])

That’s why the last element (2) gets added.
"""
