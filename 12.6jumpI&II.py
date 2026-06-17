#JUMP I
nums = [2,3,1,1,4]
maxindex=0
for i in range(len(nums)):
    if i> maxindex: # if the i is > than the max index means cant jump no more
        return False
    
    maxindex=max(maxindex,i+nums[i]) # i+the jump in the max index
    return True


#Jump II
'''
I am standing at index.

I try jump 1.
I ask recursion:
"Hey, if I land here,
what answer do you get?"

I try jump 2.
I ask recursion again.

I compare all answers.

I keep the smallest.
'''
#Brute
class Solution:
    def solve(self,index,jump,nums):
        #base case
        if index>=len(nums)-1:
            return jump

        #operation
        mini=float("infinity")

        for i in range(1, nums[index]+1):
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