#merge 2 sorted arrays distinct values

nums= [1, 2, 3, 4, 5]
arr = [1, 2, 3, 6, 7]
#i,j
i,j=0,0
merged=[]
n,m=len(nums),len(arr)
while i<n and j<m:
    if nums[i]<=arr[j]:
        if len(merged)==0 or merged[-1]!=nums[i]: # last value of merged if equal also if merged=empty so -1 index error
            merged.append(nums[i])
        i+=1 # why outside cuz if append equal will not go to next line-out of loop so we need to increment after that too
    else:
        if len(merged)==0 or merged[-1]!=arr[j]:
            merged.append(arr[j])
        j+=1
# after while loop
while j<m:# and i==n: no need for this cuz above loop will stop 
    if len(merged)==0 or merged[-1]!=arr[j]:
        merged.append(arr[j])
    j+=1
while i<n: # with if the loop doesnt run again
    if len(merged)==0 or merged[-1]!=nums[i]: # last value of merged if equal also if merged=empty so -1 index error
        merged.append(nums[i])
    i+=1
print(merged)


#cond.
#i compare with j:same, i+1,i,j compare before append if equal, whatever appended last +1, exhaust cond. 
#append


#Practice:
arr1= [3,4,5,7,9]
arr2 = [3,4,6,8,10]
result=[]
i,j=0,0
n,m=len(arr1),len(arr2)
def unique(val):
    if len(result)==0 and result[-1]!=val:
        result.append(val)
while i<n and j<m:
    if arr1[i]<arr2[j]:
        unique(arr1[i])
        i+=1
    elif arr1[i]>arr2[j]:
        unique(arr2[j])
        j+=1 
while j<m:
    unique(arr2[j])
    j+=1
while i<n:
    unique(arr1[i])
    i+=1
print(result)



#FOR UNIQUE VALUES:
#len(result) == 0------------“Is the result list empty?”
#result[-1] != val----"Is the last inserted value NOT equal to the current value?”



