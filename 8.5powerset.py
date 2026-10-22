nums=[1,2,3]
n=len(nums)#-3
totalsubsets=1<<n #2^3=8
result=[]
for i in range(0,totalsubsets): #0-7 in binary
    listsub=[]
    for j in range (0,n): #the index of binary
        if (i &(1<<j))!=0: #count bit at each index of binary:
            listsub.append(nums[j]) #the index of the binary that is bit and put it in the list
    result.append(listsub)
print(result)
