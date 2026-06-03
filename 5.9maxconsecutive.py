#Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. 
# The maximum number of consecutive 1s is 3.

# nums = [1,1,0,1,1,1]
nums=[1,0,1,1,0,1]
max_count=0
count=0
i=0
while i <len(nums): #len=1 nut numsis always len-1 so outof range and only 1 can work no need both
    if nums[i]==1: # since it only 1s #o(1)
        count+=1
        max_count=max(max_count,count) #best way to store values is compare count streaks and keep the max one
    else:
        count=0
    i+=1
print(max_count)
#TC=o(n)

#Conditions I wanted:
# count tracks the current streak.
# Reset to 0 only when a 0 interrupts it.
# max_count keeps the longest streak so far.



#if nums=[k,0,0,k,k,k,k]
nums = [5,5,5,5,0,0,5,5]
k = 5

count = 0
max_count = 0

for num in nums:
    if num == k:
        count += 1         # continue the streak
        max_count = max(max_count, count)
    else:
        count = 0          # streak broken → reset

print(max_count)



#optimized:
