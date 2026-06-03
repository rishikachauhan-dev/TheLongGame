#Transpose of a matrix:
#2x3 matrix transpose it----3x2
nums=[[5,9,1],[2,3,7]]
rows=len(nums)
col=len(nums[0])
#make empty matrix
result=[[0]*rows for _ in range(col)]#[[0,0],[0,0],[0,0]]
for i in range(0,rows):
    for j in range(0,col):
        result[j][i]=nums[i][j]
print(result)