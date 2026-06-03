matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix=[]
#result=[1,2,3,6,9,8,7,4,5]
if not matrix or not matrix[0]:
    print([])
    exit() # use when not inside a function
result=[]
left,top=0,0
bottom=len(matrix)-1 #len of row
right=len(matrix[0])-1 #actual length on col

while top <=bottom and left <=right: # when to stop? so when T and B overlaps stop loop
    for i in range(left, right+1):
        result.append(matrix[top][i]) #0, r const-append all till c,right
    top +=1

    for i in range(top, bottom+1):
        result.append(matrix[i][right])
    right -=1

    if top<=bottom: # if the matrix given in just row without this it will print it twice after left to right already printed [1,2,3]---[1,2,3,3,2,1]
        for i in range(right, left-1,-1):
            result.append(matrix[bottom][i])
        bottom -=1
    
    if left <=right: # if matrix i just a col then print twice
        for i in range(bottom, top-1,-1):
            result.append(matrix[i][left]) #till left col
        left +=1

print(result)


#optimal, sc o(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        '''
        0 col and 0 row for marking, extra space for col marking cuz it will iterfere with row marking. then for i in all matrix whenever 0 mark it, it will not see the before 0 cuz we've iterated through them.
        now loop except first row and col keep making it zero as put markings
        '''
        row=len(matrix)
        col=len(matrix[0])
        rowzero=False #if we want to zero out the 1st row
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:# if 0 found while iterating
                    if r>0: # cuz esle that box is used by col
                        matrix[r][0]=0 #in that row at col flag the row to be zeroed
                    else:
                        rowzero=True
                    matrix[0][c]=0 #same for that col

        for r in range(1,row): #inside matrix
            for c in range(1,col):
                if matrix[0][c]==0 or matrix[r][0]==0: #debugged
                    matrix[r][c]=0 #make all zeroes
        #edge case
        if matrix[0][0]==0:
            for r in range(row): # debugged
                matrix[r][0]=0 # or col same thing

        if rowzero:
            #every val in first row that is across the col
            for c in range(col):
                matrix[0][c]=0
