# Assign Cookies
'''
trick-nlogn + n (2 pointer)

while i, j in zip(g,s)
s[j]<=g[i]
ans+=1
i+1
j+1
---------'''
ans=0
i=j=0
g.sort()
s.sort()
# while i,j in zip(g,s): used in for
while i<len(g) and j<(len(s)): # i and j needs to move independently
    if s[j]>=g[i]: # candy should be = or greater
        ans+=1
        i+1 #not j+1, if 1 child not satisfied go to next child
    j+1 # cookie failed it will fail all other child when sorted so sort is imp too

print (ans)

'''
----Memory trick---
When a cookie is too small:

small cookie fails current child
↓
it will fail all future children
↓
discard cookie

---When a cookie satisfies a child:

child satisfied
cookie used up
↓
move both pointers
'''
# Fractional Knapsack Problem

'''
newlist=[v/w as ratios]
sack=0, (value)'''

items=[((i/j),i,j)for i,j in zip(val,wt) if j>0] # not floor cuz need in decimal
items.sort(key=lambda x: x[0], reverse=True )

ans=0
for r,i,j in items:
    if capacity>=j:
        ans+=i
        capacity-=j
    else:
        ans+=r*capacity
        break # to stop else capacity is not subrated will use the left capacity again to add the fractional value
print(ans)
    
# Greedy algorithm to find minimum number of coins
'''reverse the denomination 1-10
then for n cant change money=n
money-i in denomination till money>=i ans+=1
else i+1'''
# Lemonade Change

'''lemonade cost=5
five= ten= twenty=0
for i in bills:
if i==5
five+=1
elif i==10:
    ten+=1
    if five>=1
        
    else False
else i==20
    if ten>1 and five>=1:
    ten-=1
    five-1
    elif five>=3:
        five-=3
    else:
    False
True
'''
# N meetings in one room
'''
sort on based of start time, make a new list with pairs based on start time
loops finish=j, start=i,
while i < len(start) and j< len(finish)
last activity=0
    if j<i
    count+=1
    else:
        skip--pass
-------
meeting=[]
for i in range(len(finish)):
    meeting.append(finish[i],start[i])

meeting.sort()
lastend=[0][0]
count=1(can always fit 1 meeting)
for i range(1,len(finish) #while i< len(meeting): last meeting stored
    currend=meeting[i][0]
    currstart=meeting[i][1]
    if currstart>lastend:
        count+=1

        lastend=currend
return count

'''

# Jump Game
'''
currentindex vs maxindex it {currindex+nums[currentindex]} reached, so if curr> maxindex means the maxindex couldnt reach to the end of the list
'''
# Jump Game 2
'''min jumps
Brute-
base case
for i till the number in that curr index,
 mini=min(mini. recursive call of all possibilitis of i index)
 then i+1?'''

# Minimum number of platforms required for a railway
'''
Brute:
    for every i check all dep(j) if < than i count=1 if not count+=1
    maxi count
-----------
j for dep and i for arr
    if j<i count-1 keep the same plat dep jldi ho rha hai, check or konse jldi dep hai fro the same i
    j>i dep too late count+1 add a new plat, check for same j if start is early than dep
    max count
'''