'''
total=0
maxi
loop i check if next element is in hashmap if not add and increase count
total=3
'''
# Brute--TC failed for some only works if we want subsequence
s = "pwwkew"
# s="abcabcbb"
myset=set()
for i in s:
    myset.add(i)
# return len(myset)
print(myset)

# Brute sol:
# ques- set vs hashmap()-dict??- we take set cuz we want to confir if it is already in the result, dont want index etc
#Brute
if not len(s):
    return 0
maxi=0
for i in range(len(s)):
    set={} # needs reset after each loop-cant have set it does not contain duplicate, so dict
    for j in range(i,len(s)):
        if s[j] in set:
            break 
        maxi=max(maxi,j-i+1)
        set[s[j]]=1
        # myset.add(tuple(s[j]))
return maxi

#optimal
'''
left and right both at 0, r++
if r already in dict? if not ---maxi=max(maxi,r-l+1)
if yes make it valid?- l+1 till l==that no. +1, not r-1
dict?? r++ append it with index cuz when duplicate found by r, l skips to front and updates the dict keys values

for r till n:
    if r in myset (for every r):
        (if found then it was at which index??)
        v=set[r]
        l++ till v then l+1
    maxi=max(maxi,r-l+1)
    set[s[r]]=r
return maxi
'''
s = "abcabcbb"
l=0
r=0
maxi=0
n=len(s)
set={}
while r<n: # forgot to increment r
    if s[r] in set:
        # v=set[s[r]]
        # while l<v:
        #     l+=1
        # l=+1 #skip after 
        '''not this but'''
        l=max(l,set[s[r]]+1) # why 1 cuz it same as original logic l+1
    maxi=max(maxi,r-l+1)
    set[s[r]]=r # updated here even if found or not to current r
    r+=1
print(maxi)