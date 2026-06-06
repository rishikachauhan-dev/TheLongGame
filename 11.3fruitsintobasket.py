fruits = [1,2,1]
# Output: 3
# fruits = [1,2,3,2,2]
# Output: 4
'''
b1,b2 as dict
for i in fruits, 
check if already exist in b1 or b2-append:
if does not exist in either
empty baskets, move i till window end, keep track of max counts

'''
right=0
left=0
maxi=0
b1={}
b2={}
while right < (len(fruits)):
    if fruits[right] in b1:
        b1[fruits[right]]+=1
    elif fruits[right] in b2:
        b2[fruits[right]]+=1
    else:
        b1.clear()
        b2.clear()
        left=max(left,right)
    maxi=max(maxi,(b1[fruits[right]]+b2[fruits[right]]))  # cant do this lol  
    right+=1
print(maxi)

#Brute----------
'''for every i iterate j and add to set of len(set)> 2, i++'''
#Better-while instead of if
#Optimal-if----------
left=0
right=0
mydict={}
maxi=0
while right <len(fruits):
    mydict[fruits[right]]=mydict.get(fruits[right],0)+1 # if key exists ok, else 0 then +1
    if len(mydict)>2:
        mydict[fruits[left]]-=1
        if mydict[fruits[left]]==0:
            del mydict[fruits[left]]
        left+=1
    maxi=max(maxi,right-left+1)
    right+=1
return maxi

