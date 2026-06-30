#JUMP I
nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
maxindex=0
for i in range(len(nums)):
    if i> maxindex: # if the i is > than the max index basically out of the len means cant jump no more
        return False
    
    maxindex=max(maxindex,i+nums[i]) # i+the jump in the max index
    return True


#Jump II
'''
At index 0:
nums[0] = 2

Can jump:
1 step
2 steps

So your brain should think:
Should I jump to 1?

or

Should I jump to 2?
Let's try both.
Whichever reaches the end in fewer jumps wins.

'''
#Brute
class Solution:
    def solve(self,index,jump,nums):
        #base case
        if index>=len(nums)-1:
            return jump

        #operation
        mini=float("infinity")

        for i in range(1, nums[index]+1): # for i till th number in that curr index i is the jump
            mini=min(mini,self.solve(index+i,jump+1,nums))# debugged i was 1
        return mini

    def jump(self, nums: List[int]) -> int:
        return self.solve(0,0,nums)
#TLE
#o(n^n)
#o(n)

#Optimal
nums = [2,3,1,1,4]
j=i=jump=0
while j<len(nums)-1:
    farthest=0
    for n in range(i,j+1): # 2 pointers
        farthest=max(farthest, n+nums[n])
    i=j+1 #indentation error
    j=farthest
    jump+=1
return jump

# Each index enters the inner loop exactly once across all iterations, 
# so the total cost is O(n) for the scans plus O(n) for boundary updates, which is O(n + n).
# Simplified: O(n) time.

# Space: Only a few variables are used, so O(1) extra space.