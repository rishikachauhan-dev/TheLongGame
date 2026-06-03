'''
This is:
variable value
vs
object mutation

sum changes during recursion
→ so maybe we need sum.copy()

Integers are NOT mutated
When you do:
sum + arr[ind]
Python creates a new integer.
It does NOT modify old sum.

Happens with lits or mutable objects-like list dict etc.

| Type | Mutable? | Needs copy?  |
| ---- | -------- | ------------ |
| list | ✅ yes    | ✅ yes        |
| dict | ✅ yes    | ✅ yes        |
| int  | ❌ no     | ❌ impossible |
| str  | ❌ no     | ❌ no         |
'''
class Solution:
    def solvesum(self,ind,sum,arr,result):
        if ind>=len(arr):
            result.append(sum)
            return
        
        # operation
        # subset.append(arr[ind]) no need for this
        # sum+=arr[ind]-add that to fucntion cuz backtracking on sum not needed
        
        #pick
        self.solvesum(ind+1,sum+arr[ind],arr,result)
        
        # subset.pop()
        # sum-=arr[ind]
        
        self.solvesum(ind+1,sum,arr,result
             
	def subsetSums(self, arr):
		result=[]
		self.solvesum(0,0,arr,result)
		return result



'''
In this subset sum problem:
there is NO explicit backtracking line for total

because:
recursion stack automatically restores it

Then what IS the backtracking?

This:
return

When recursive call finishes,
Python goes BACK to previous stack frame.

That is the backtracking.

THIS is implicit backtracking
Return restores previous function state automatically
'''
# Recursion itself backtracks.
# pop() only fixes shared mutable objects.

'''
| Implicit                    | Explicit             |
| ------------------------    | -------------------- |
| recursion stack restores    | you restore manually |
| immutable state: sum,int etc| mutable state: list, dict etc|
| no undo line                | undo line required   |
| automatic                   | manual               |
'''