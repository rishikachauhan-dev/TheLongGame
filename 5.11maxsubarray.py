#Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#Brute
nums = [-2,1,-3,4,-1,2,1,-5,4]

maxi=float('-infinity')
for i in range(0,len(nums)):
    total=0 # inside cuz we want it to reset
    for j in range(i,len(nums)): 
        total+=nums[j] #add to the sum
        if total>maxi:
            maxi=total
        # maxi=max(maxi,total)
print(maxi)

#Tc=o(n^2) sc=o(1)

#Optimal
n=len(nums)
total=0
maxi=float('-infinity')
for i in range(0,n):
    total=total+nums[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
print(maxi)

# since every cal was done in 1 line o(n) sc=o(1)



#practise
arr1= [-2,1,3,6,9,-1,-9,-5]
maxt=float('-infinity')
for i in range(0,len(arr1)):
    total=0
    for j in range(i+1,len(arr1)):
        total=total+arr1[j]
        maxt=max(maxt,total)
print(maxt) #n^2

#kandane-if useless-skip
arr2= [-2,1,3,6,9,-1,-9,-5]
maxs=float('-inf')
total=0
for i in range(0,len(arr2)):
    # if arr2[i]>0:
    #     total=total+arr2[i]
    #     maxs=max(maxs,total)
    # else:
    #     total=0
    total=total+arr2[i]
    maxs=max(total,maxs)
    if total<0:
        total=0
print(maxs)
#but this is not kadane as its resetting looking the element if its negative
#kadane=if total is negative, Why? Because negative numbers can still be part of the best subarray.

