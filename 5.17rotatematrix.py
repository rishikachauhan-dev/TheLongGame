#Rotate matrix by 90
matrix=[[1,2,3,4],[5,6,7,8],[9,8,10,11,12],[13,14,15,16]]



#Brute force
n=len(matrix)
m=len(matrix[0])
result=[[0 for _ in range (0,m)] for _ in range(0,n)]#SC-nxn
# print(result)
for i in range(0,n):
    for j in range(0,m):#nxn
        result[j][(n-i)-1]=matrix[i][j]
print(result)
#Tc=n^2 Sc=n^2

#Optimal
r=len(matrix)
c=len(matrix[0])
for i in range(0,r): #nxn
    # for b in range(a+1,y): #uppertriangle
    for j in range(0,i): #lowertriangle-i>j j till i
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] # swap
    matrix[i].reverse() #nxn for a matrix every element in row then in column
print(matrix)
#o(2n^2)   o(n)