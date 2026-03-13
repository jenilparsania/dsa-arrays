"""
interchanging of rows and columns in a matrix

5,9,1    => 5 2
2,3,7       9 3
            1 7


"""
nums = [[5,9,1],[2,3,7]]
rows = len(nums)
cols = len(nums[0])
result = [[0]*rows for _ in range(cols)]
res_cols = len(result[0])
res_rows = len(result)

for i in range(rows):
    for j in range(cols):
        result[j][i] = nums[i][j]
    print()

for i in range(res_rows):
    for j in range(res_cols):
        print(result[i][j],end=" ")
    print()