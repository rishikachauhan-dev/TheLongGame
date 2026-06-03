#return index of target value
#return index of first ocuurance of target value if duplicates then if it actally exists?

nums=[10,3,10,8,4,10]
k=8 #target value
for i in range(len(nums)):
    if nums[i]==k: #o(n)
        break
    else:
        print(-1)
print(i)
 # -1 not found

# works for duplicate too
#dont complicate

#Tc=o(n)

# ? Why
nums=[10,3,10,8,4,10]
k=3
for j in nums:
    if j==k:
        break
    else:
        print(-1)
print(nums.index(j))

#The else is inside the loop, so on the first iteration itself:
# If the first element isn’t equal to x,
# it immediately returns -1,
# without checking the rest of the array.

nums=[10,3,10,8,4,10]
k=4
for i in nums:
    if i == k:
        print(nums.index(i))
print(-1)# this wroksx only with return elxse none


#practise:
arr=[10,99,10,8,4,101]
k=101
for n in arr:
    if n==k:
        print(arr.index(n))
