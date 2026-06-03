#createv a newlist #cond=equal pos and neg
#Brute force
nums=[5,10,-3,-1,-10,6]
n=len(nums)
pos=[x for x in nums if x>0] #o(n)
neg=[x for x in nums if x<0]#o(n)

for i in range(0,len(neg)):# not n but len(pos)/neg list cuz we are iteratine these 2 to be put in nums
    nums[2*i]=pos[i]
    nums[(2*i)+1]=neg[i]
print(nums)
#o(n/2)=o(5n/2) # list slice is n/2


#Optimal   #3pointer
arr=[5,10,-3,-1,-5,7]
m=len(arr)
newlist=[0]*m
pos,neg=0,1
for i in range(0,m):
    if arr[i]>0:
        newlist[pos]=arr[i]
        pos+=2
    else:
        newlist[neg]=arr[i]
        neg+=2
print(newlist)
# Tc=o(n) Sc=o(1)
        
