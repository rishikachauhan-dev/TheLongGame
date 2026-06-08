val = [60, 100, 120]
wt= [10, 20, 30]
capacity = 50
# Output: 240.000000

# val= [500]
# wt= [30]
# capacity = 10

''''
i=j=total=0

while i < len(val) and j< len(wt):
    #add to capacity and i to total
    if capacity<wt[j]:
        b=(val[i]//wt[j])*capacity
        total+=b
    total+=val[i]
    capacity-=wt[j] # last
    i+=1
    j+=1
print(total)
'''
items=[(v/w,v,w) for v, w in zip(val,wt) if w>0] # make list of ratio and w>0 to avoid 0 devision
#sort items by ratio, which is at 0 index and in descending order
items.sort(key=lambda x: x[0], reverse=True)
currwt=0
totalval=0
for ratio,v,w in items:
    if currwt+w<=capacity: # add all weights to currwt till capacity>0

        currwt+=w
        totalval+=v
    else:
        remain=capacity-currwt
        if remain<0: # if full capacity reached already
            break
        totalval+=ratio*remain
        break # this break cuz if there were more no need to iterate till end since we ran out of capacity
print(totalval)