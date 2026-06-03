#Better-self
nums=[1,99,101,98,2,5,3,100,1]
nums.sort() # sorting is logn
# print(nums)
maxi=0
count=0
for i in range(1,len(nums)):
    if nums[i-1]+1==nums[i]:# not countig elements but difference thats why 3
        count+=1
        maxi=max(maxi,count)
    else:
        count=0 
print(maxi+1)

#TC=o(nlogn+n)~nlogn # this is the better sol

# O(n) = you walk through the list once
# O(n log n) = you walk through the list more than once in a structured (divide & conquer)


# A set is a data structure that:

# ✅ Stores unique items only
# ✅ Has no duplicates
# ✅ Is unordered (no index)
# ✅ Offers O(1) lookup time (super fast)

# Think of a set like a bag of unique values.
# If we used a list:
# Checking membership each time → O(n)
# Looping + membership check → O(n²) ❌

# But with a set:
# Membership → O(1)
# Total → O(n) ✔

nums = [1,99,101,98,2,5,3,100]
myset = set(nums) #TC: O(n) SC: O(n) (set stores all unique elements of list to set, could be n in worst case)
longest = 0
for num in myset: #o(n)
    if num-1 not in myset:#lookup
        x=num
        count=1 #resets here
        while x+1 in myset:#o(n) why not n^2 cuz increment right? but worst case is that all are unique values so 1,2,3,5,6,7,2 after 2 1 already exists
            count+=1
            x+=1
        longest=max(longest,count)
print(longest)
#Tc=o(3n) sc=o(n)-cuz of the set