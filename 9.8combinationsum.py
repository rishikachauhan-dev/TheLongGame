'''n^n 
braching will happen for each index till 
total==target or index>length--base case with filter too then append it to the result

same subset loop, inside recursion another recursion
filter-if in result'''

'''funct(subset):
    base case-index>=length
        total==target
            if in result skip else append
    
    operation
    subset=arr[index]
    total=arr[index]

    choice 1
    call func(func())

    backtrack
    subset.pop()
    total-=arr[index]

    choice 2
    call(call)
return result 
'''
class Solution:
    def combsum(self,ind,sum,subset,candidates,target,result):
        #base case
        if ind==len(candidates):
            if sum==target:
                result.append(subset.copy())
                return
            return
        elif sum> target:
            return
        
        #operation
        subset.append(candidates[ind])

        #pick
        self.combsum(ind,sum,subset,candidates,target,result) # using the same index till len

        #backtrack
        subset.pop()

        #notpick
        self.combsum(ind+1,sum+candidates[ind],subset,candidates,target,result)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.combsum(0,0,[],candidates,target,result)
        return result

#but TLE so____
class Solution:
    def combsum(self, ind, total, subset, candidates, target, result):
        
        # base case
        if total == target:
            result.append(subset.copy())
            return
        
        if total > target or ind == len(candidates): #!!!!!!!
            return
        
        # pick (only if valid)
        if candidates[ind] <= target: #!!!!!!
            subset.append(candidates[ind])
            self.combsum(ind, total + candidates[ind], subset, candidates, target, result)
            subset.pop()
        
        # not pick
        self.combsum(ind + 1, total, subset, candidates, target, result)
    
    def combinationSum(self, candidates, target):
        candidates.sort()  # 🔥 important 
        ''' we are sortinf the nums so that loop doesnt break for the candidates[ind] <= target condition
        eg: candidates = [7, 2, 9, 3]
            target = 6
            At index 0:
            7 > 6 ❌
            But you can’t stop, because later:
            2, 3 might work ✅
            👉 So recursion must continue → wasted calls
            therefor sort
                    '''

        result = []
        self.combsum(0, 0, [], candidates, target, result)
        return result
