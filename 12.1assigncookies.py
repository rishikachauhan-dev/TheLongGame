g = [1,2,3]
s = [1,1]
# Output: 1
# g = [2,4]
# s = [1,2,3]
# Output: 1

#Brute
'''
for j in s if g[i]>=j then assign, if not check for next element
check min no. of cookie satisfied
count+=1
better=sort both
'''
g.sort()
s.sort()
''''
# mini=float('infinity')
# for i in g and for j in s: this---
i = j = count=total=0
while i < len(g) and j < len(s):
    if j>=i:
        count+=1
        j+=1 # wrong here too when the child is satisfied which pointer to move?
    i+=1
print(count)'''

#Brute/Optimal-sort first
i = j = count=0
while i < len(g) and j < len(s): # debugged was comparing in dexes
    if s[j]>=g[i]:
        count+=1
        i+=1 # debuged -child satisfies if not else cond. for j
    j+=1
print(count)
