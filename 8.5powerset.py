n=len(nums)#-3
totalsubsets=1<<n #2^3=8
result=[]
for bin in range(0,totalsubsets): #0-7 in binary
    listsub=[]
    for i in range (0,n): #the index of binary
        if (bin &(1<<i))!=0: #count bit at each index of binary:
            listsub.append(nums[i]) #the index of the binary that is bit and put it in the list
    result.append(listsub)
print(result)
