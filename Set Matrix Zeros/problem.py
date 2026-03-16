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





def setZeros(matrix)->None:
    def makeInfinity(matrix,row,col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        for j in range(0,c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")
        
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j] == 0:
                makeInfinity(matrix,i,j)


    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
    
    return matrix


nums = [[1,2,3],[11,12,13],[21,0,23]]
print(setZeros(nums))

"""
TC -> O((N+M)*(N*M)) + O(N*M) 
SC -> O(1)
"""
    


