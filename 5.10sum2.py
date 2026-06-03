#in a list return 2 no. whose sum is target
#a no. can repeat only once

num=[5,9,3,2,4,6,1]
target=13
#Brute force
n=len(num)
for i in range(0,n-1): #exclusive with that too it will go till 8 cuz we will be moving j till 7: else -Index error
    for j in range(i+1,n):#better i+1 than 1 cuz if i=2 it will start again from 1
        if num[i]+num[j]==target:
           print(i,j)
#Tc=o(n(n=1)/2)=n^2 sc=o(1)

#Optimal
n=len(num)
hashmap={}
for i in range(0,n):
    remain=target-num[i]
    if remain in hashmap: #lookup
        print(hashmap[remain],i)# remain value cuz already there, i curent index
    hashmap[num[i]]=i



# ✅ Why do we look back (in hashmap) and not scan the whole list?
# Because the idea is:

# “As I move forward, store what I have seen.”
# “Whenever I see a new number, check if its partner already appeared.”

# WHY LOOK BACK ONLY?
# Because looking back is enough.
# The correct partner must be:
# already seen
# stored in hashmap
# You don’t need to search the whole list again.

# Because checking the whole list every time is:
# O(n) per iteration
# O(n²) total → too slow
# Instead, hashmap lookup is:
# ✔ O(1)
# So total = O(n).