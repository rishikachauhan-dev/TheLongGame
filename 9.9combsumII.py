#BRUTE-------------

''''class Solution: 
    def solve(self,ind,total,subset,candidates,myset,result,target): 
        # base case 
        if ind>=len(candidates): 
            if total==target: 
                subset.sort()
                if subset in myset: 
                    return myset.add(subset.copy()) 
                result.append(myset) 
            return 
        return 
        if total>target: 
            return 

        #operation 
        subset.append(candidates[ind]) 
        total+=candidates[ind] 

        #pick 
        self.solve(ind+1,total,subset,candidates,myset,result,target) 
        subset.pop() #backtrack 

        # not pick 
        self.solve(ind+1,total,subset,candidates,myset,result,target) 

        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
            myset=set()
            result=[]
            self.solve(0,0,[],candidates,myset,result,target)
            return result
            
🔴 What’s going wrong

❌ 1. You mutate total in-place
total += candidates[ind]
...
self.solve(...)
...
self.solve(...)  # ❌ uses modified total
👉 The not-pick branch is using the wrong sum.

❌ 2. You try to put a list in a set
myset.add(subset.copy())  # ❌ list is unhashable-- cant add list in tuple

❌ 3. Wrong thing appended to result
result.append(myset)  # ❌ appending whole set

❌ 4. Duplicate handling is weak
subset.sort()
if subset in myset:
👉 Sorting every time is expensive and still not robust.'''

class Solution:
    def solve(self, ind, total, subset, candidates, myset, result, target):
        
        # base case
        if ind >= len(candidates):
            if total == target:
                key = tuple(subset)
                if key not in myset:
                    myset.add(key)
                    result.append(subset.copy())
            return
        
        if total > target:
            return
        
        # pick
        subset.append(candidates[ind])
        self.solve(ind + 1, total + candidates[ind], subset, candidates, myset, result, target)
        
        # backtrack
        subset.pop()
        
        # not pick
        self.solve(ind + 1, total, subset, candidates, myset, result, target)
    
    def combinationSum2(self, candidates, target):
        candidates.sort()  # important for duplicates
        myset = set()
        result = []
        self.solve(0, 0, [], candidates, myset, result, target)
        return result

#TLE-
'''WHy? Its is generating everydebset first checking then not adding it to the result'''


#OPTIMAL-----for loop backtracking
'''Loop movement = duplicate skipping
Recursive call = picking'''

nums=[1,1,1,2,2,3,6]
target=6

class Solution:

    def solve(self,ind,target,nums,subset,result):
        if target==0:
            result.append(subset.copy())
            return
        if ind>len(nums):
            return
        
        #operation
        for i in range(ind,len(nums)):
            if i>ind and nums[i]==nums[i-1]: #duplicates skipping
                continue

            if nums[i]>target:
                break

            subset.append(nums[i])
            self.solve(i+1, target-nums[i],nums,subset,result)#i = actual chosen element not ind
            subset.pop()

    def combsum2(self, nums, target):
        nums.sort()
        result=[]
        self.solve(0, target,nums,[],result)
        return result

