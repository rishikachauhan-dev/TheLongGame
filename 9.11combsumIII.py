class Solution:
    def solve(self,last,sum,n,k,subset,result):
        #base case
        if sum==n and len(subset)==k: #both must be true
            result.append(subset.copy())
            return
        
        if sum>n or len(subset)>k:
            return
        #operation
        for i in range(last,10): #last index
            subset.append(i)
            self.solve(i+1,sum+i,n,k,subset,result) #1+1-start from 2--
            subset.pop()#bactrack

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.solve(1,0,n,k,[],result) #start with 0 last=1
        return result