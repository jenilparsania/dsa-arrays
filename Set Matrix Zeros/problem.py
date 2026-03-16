"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

def printMatrix(nums):
    rows = len(nums)
    cols = len(nums[0])

    for i in range(rows):
        for j in range(cols):
            print(nums[i][j],end=(" "))
        print()
# first iteration for marking the rows and cols to infis
# second iteration for changing the infis to zero


nums = [[7,8,3],[17,18,13],[27,0,23]]
tracker = []
printMatrix(nums)
rows = len(nums)
cols = len(nums[0])

for i in range(rows):
    for j in range(cols):
        if nums[i][j] == 0:
            tracker.append([i,j])

printMatrix(tracker)

