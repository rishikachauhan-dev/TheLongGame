# Largest Element in an Array
'''
max=float(-'infinity'), for in nums comare every i with max and get max number

o(n)
o(1)
'''
# Second Largest Element in an Array without sorting
'''
same
2: max1 and max2
for i in nums max 1 largest if found another larger then put max1 to max2

o(n)
o(1)
'''
# Check if the array is sorted
'''
for i in nums and j+1 till n if j+1 > i if not then False

o(n)
o(1)
'''
# Remove duplicates from Sorted array
''' move duplicates to last

swap- i will find the next element and j will stay on the last unique one
for i in nums 0 to n, j and i can start from 0
while j<=n
when i!=i-1 stop, swap with j+1
j++ only after swapping
else i++

o(n)
o(1)
'''
# Right Rotate an array by one place
'''
brute:
[3,4,5,6,8]
pop and insert last element

o(kn),o(1)

optimal: reverse pointer
 i at last element temp
 shift element to right swap [i+1]=[i]
 nums[0]=temp

'''
# Right rotate an array by K places
'''
brute:pop and insert till k==target- o(kn) for k loop k times then nums insert for each k each element n times shift

better: slicing??---nums[:]=nums[n-k:]+nums[:n-k]
o(k-n +k)=o(n)

optimal:
from (0:n-k) , (n-k+1:) k/2 + (n-k)/2
i and j from each last swap
then swap all, not recursive 'create a function thats all'

k%n==k then target is 1 so let the loop run k=k%n

o(n)
'''
# Move Zeros to end
'''
till i!==0 i++, when found swap with j+1
then j=i
i,j=0

o(n)
'''

# Linear Search
'''
for i till n if nums[i]==target return i else return -1

o(n)
'''
# Merge 2 sorted Arrays
'''
if already sorted for i in arr1 and j in arr2 compare each at append to result i++ then j++ leftover elements
'''
# Find missing number in an array
'''
optimal:
difference of sum of number 0 to n and sum of number in nums 
'''
# Maximum Consecutive Ones
'''
count max consecutive 1

count=0 and a max_count
for i in range nums 
    if nums[i]==nums[i-1] or nums[i]==1 or k
    count +=1
    max(maxcount,count)
    else
    reset count

o(n)
o(1)
'''