#BRUTE

nums=[1,2,4]
# new=[1,2,3,4]
for i in range(len(nums)+1): # cuz mising so len should be+1 then original o(n)
    if i not in nums: #o(n)
        print(i)
#Tc=o(n^2)
# Time Complexity:O(n2) in the worst case because:
# We are iterating from 0 to n (which is n+1 iterations).
# Each membership check (i not in nums) is O(n) for a list.

#BETTER

'''By dict hashmap
o(n) but space o(n)'''


#optimal
''' difference of sum of number 0 to 3 and sum of number in nums 
'''
n = len(nums)
original_total = (n * (n + 1)) // 2 #sum of n numbers

number= original_total - sum(nums)
print(number)