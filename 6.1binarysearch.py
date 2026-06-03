nums=[2,4,6,7,9,11,18,19]
n=8
target=6
## first by for loop/ITERATIVE METHOD
low=0
high=len(nums)-1

while low<=high:
    m=(low+high)//2
    if nums[m]==target:
        print(nums[m])
        break
    elif nums[m]<target:#mid smaller than target means the ans is in higher side--eliminate lower side
        low=m+1
    else:
        high=m-1
    
print(-1)

nums=[2,4,6,7,9,11,18,19]
n=8
target=13
##By recursion
def bs(nums,low=0,high=n-1):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return bs(nums,mid+1,high)
    else:
        return bs(nums,low,mid-1)
print(bs(nums,low=0,high=n-1))