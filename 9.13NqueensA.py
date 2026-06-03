'''generate all the possibilities putting queens on each row keeping col const in each recursive call'''


'''first make a board eg n=4, nxn '''
class Solution:
        
    n=4
    ans=[]
    board=["." * n for _ in range(n)]

    def solve(self,col,board,ans,n):
        #base case
        if col==n:
            ans.append(list(board))
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row]=board[row][:col]+"Q"+board[row][col+1:] 
                #in the board matrix[row][col], const row, :col=all before col, replace Q after that, than continue with '.. skipping the exluded col'
                #'..Q..' eg.
                self.solve(col+1,board,ans,n)

                board[row]=board[row][:col]+"."+board[row][col+1:] # Q not here # undo part

        def isSafe(self,row,col,board,n):
            duprow=row
            dupcol=col

            #check upper-left diangonal
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1

            # # Reset and check left row
            col=dupcol
            row=duprow
            while col>0:
                if board[row][col]=="Q":
                    return False
                col-=1

            #reset then check left lower
            row=duprow
            col=dupcol
            while row<n and col>=0:
                if board[row][col]=="Q":
                    return False
                row+=1
                col-=1
            return True
             


                
