# nums = [1,3,5,6]
# target = 5
nums = [1,3,5,6]
target = 2
low=0
high=len(nums)-1
ind=len(nums)
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:# cux if no there it will be the index of the next largest element
        ind=mid
        high=mid-1
    else:
        low=mid+1
print(ind)
