"""
5   10  8
    6   3
        9


"""

nums = [[5,20,3],[7,-10,9],[1,-52,6]]
row = len(nums)
cols = len(nums[0])

for i in range(0,row):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    
    print()
