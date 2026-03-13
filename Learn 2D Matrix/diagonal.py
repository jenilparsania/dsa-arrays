nums = [[5,10,8],[7,6,3],[2,1,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(rows):
    for j in range(cols):
        if i == j:
            print(nums[i][j],end=" ")
        else:
            print(" * ",end=" ")
    print()