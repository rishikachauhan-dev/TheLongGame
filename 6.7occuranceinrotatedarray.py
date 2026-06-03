arr=[4,5,6,7,0,1,2]
target1=10
for i in range(len(arr)):
    if arr[i]==target1:
        print(i)
        break
else: print(-1) #here else belongs to the for loop

#if rotated it will be sorted
nums=[10,7,6,0,1,2,3]
target=7
low=0
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(mid)
        break
    #if mid to high ascending?
    if nums[mid]<=nums[high]:
        #check if target in here?
        if nums[mid]<=target<=nums[high]:
            low=mid+1 #eleminate left side array
        else:
            high=mid-1 # eleminate left arr
    else: # if low-mid
        #check target in here
        if nums[low]<=target<=nums[mid]: #o(1) lookup
            high=mid-1
        else:
            low=mid+1
else:
    print(-1) # with the loop
#Sc=o(1)