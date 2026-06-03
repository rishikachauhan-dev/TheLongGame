#Brute but TLE
arr= [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
ans=[-1]*len(arr)
for i in range(0,len(arr)): #end is exclusive
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            ans[i]=arr[j]
            break #stops else it will find another greater no.
            
print(ans)

#optimal
class Solution:
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        ans=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1): #first is inclusive
            while len(stack)!=0 and stack[-1]<=arr[i]: #len check for insed error and 
            #pop untill the previous element small
                stack.pop()
            if len(stack)!=0:
                ans[i]=stack[-1]
            
            stack.append(arr[i])
        return ans
#---------------------------------
# Leetcode Circular search
nums = [1,2,1]
# Output: [2,-1,2]
nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

# brute❌
n=len(nums)
ans=[-1]*n
for i in range(n):
    for j in range (i+1,n):
        if nums[j]>nums[i]:
            ans[i]=nums[j]
            break
    for j in range(n-1):
        if nums[j]>nums[i]:
            ans[i]=nums[j]
print(ans)
#o(n^2)


#optimal
n=len(nums)
result=[-1]*n
stack=[]
for i in range(2*n-1,-1,-1): #twice in the index of the same list
    while len(stack)!=0 and stack[-1]<=nums[i%n]: #i modulus that its fits itni the same index else out of range
        stack.pop()
    if i<n: #when it reaches the ACTUAL index
        if stack: # not while o(1)-if
            result[i]=stack[-1]
    stack.append(nums[i%n])
print(result)
#o(n)
#o(n)