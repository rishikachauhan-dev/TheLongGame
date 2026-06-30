#max consecutive II------------
# You are given a binary array nums that contains only 0s and 1s. 
# You need to find the maximum number of consecutive 1s that you can get if you are allowed to flip at most one 0 to 1.
# nums = [1, 0, 1, 1, 0]
nums = [1,1,0,1,0,1,1]
# nums = [0,0,1,1,1]
n=len(nums)
left=0
right=0
maxi=0
count=0
while right <n:
    count +=nums [right]^1
    if count>1:
        left=max(left,right)
        count=0
    maxi=max(maxi,right-left+1) 
    right+=1
print(maxi)
'''
left = max(left, right)
Since:
right >= left
almost always,
this becomes:
left = right
So whenever you see a second zero, you jump left directly to right.
in 2nd case: chanced  left could have started from 3rd index not 4th where the righfound another 0
this doesnt work cuz here we are not seeing if its 1 or 0 when moving left
'''

left = 0
zeros = 0
ans = 0

for right in range(len(nums)):
    zeros += nums[right] ^ 1

    while zeros > 1:
        zeros -= nums[left] ^ 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)

#o(n)
#o(1)
#max consecutive III------------
'''Brute force will be- for each i move j rigt till max it can form -o(n^2)'''
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# Output: 6

#Optimal
n=len(nums)
right=0
left=0
maxi=0
zeroes=0
while right <n:
    if nums[right]^1==1:
        zeroes+=1
    if zeroes>k:
        zeroes-=nums[left]^1
        left+=1
    maxi=max(maxi,right-left+1)
    right+=1
print(maxi)
#o(n)
#o(1)

