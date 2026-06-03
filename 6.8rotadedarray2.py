#edge case--has dupilcates-- problem if cant compare then low or high which side will they go?
# nums = [2,5,6,0,0,1,2] 
nums=[4,5,6,6,7,0,1,2,4,4]
nums=[1,0,1,1,1]
target = 0
# target = 4
low=0
high=len(nums)-1
left=-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        # left=1
        break
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
        continue
    #acending side low to mid
    if nums[low]<=nums[mid]:
        #check if target is in here?
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else: low=mid+1
    else: #right side
        if nums[mid]<=target<=nums[high]:
            low=mid+1
        else: high=mid-1
print(True if left==1 else False)