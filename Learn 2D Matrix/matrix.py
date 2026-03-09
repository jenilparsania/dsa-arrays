# 2D matrix
#  how to represent a matrix ? 
# nums = [[5,20,3],[7,-10,9],[1,-52,6]]
# rows = len(nums)
# columns = len(nums[0])

# iterating
nums = [[5,20,3],[7,-10,9],[1,-52,6]]
# rows : i , columns : j

rows = len(nums)
cols = len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j],end=" ")
    print()
