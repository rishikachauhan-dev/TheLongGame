n=4
class Solution:
    def isSafe(self,row,col,board,n):
        #resets to default these here are curr val of Q to be placed
        duprow=row
        dupcol=col

        #upp-diagonal left:
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False #not safe
            col-=1
            row-=1

        #check left
        #reset
        row=duprow
        col=dupcol
        while col>=0:
            if board[row][col]=='Q':
                return False #not safe
            col-=1
        #check bottom-leftdiagonal
        #rest to curr
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=='Q':
                return False #not safe
            col-=1
            row+=1
        return True
    def pos(self,col,board,result,n): # no need for row as it will be the next list 
        #base case -when all col tried and foun
        if col==n:
            result.append(list(board)) #copy of current board state
            return
        #operation
        for row in range(n): #recursive loop
            if self.isSafe(row,col,board,n): #==True: # always run for true
                board[row]=board[row][:col]+'Q'+board[row][col+1:] #this is the append
                #backtrack-the recursive loop
                self.pos(col+1,board,result,n)# at each col increment for loop for row+1
            #else-automatic-cuz above recursion runs first when false
                board[row]=board[row][:col]+'.'+board[row][col+1:] 

    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=['.'*n for _ in range(n)] #board list
        self.pos(0,board,result,n)
        return result
        