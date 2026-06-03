#Brute
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r=len(matrix)
c=len(matrix[0])
def makeinf(matrix,row,col):#i,j diff than r,c obv naming i,j as row,col
    for i in range(r):
        if matrix[i][col]!=0:#this way col will be same instead of putting j
            matrix[i][col]=float('inf')
    for j in range(c):
        if matrix[row][j]!=0:#this way col will be same instead of putting j
            matrix[row][j]=float('inf')
#o(n+m)
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j]==0:
                makeinf(matrix,i,j) #o(nxm) each element 3x4=12
#making inf 0
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j]==float('inf'):
            matrix[i][j]=0
print(matrix) #o(nxm)
#Tc=o() sco(1)



#better
#matric = [[0,1,2,8],[3,4,0,2],[1,3,1,5]]
matric = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r=len(matric)
c=len(matric[0])
rowtrack=[0 for _ in range(r)]
coltrack=[0 for _ in range(c)]
for i in range(0,r):
    for j in range(0,c):
        if matric[i][j]==0:
            rowtrack[i]=-1
            coltrack[j]=-1
for i in range(0,r):
    for j in range(0,c):
        if rowtrack[i]==-1 or coltrack[j]==-1:
            matric[i][j]=0
print(matric)
#Tc=o(2(nxm))~(nxm)  Sc=o(n+m) 2 spaces with same rows and col only rowtrack