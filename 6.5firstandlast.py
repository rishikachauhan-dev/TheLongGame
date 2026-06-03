nums = [5,7,7,8,8,10]
target = 20

#BRUTE
# low=0
# high=len(nums)-1
# first=-1
# last=-1
# for i in range(len(nums)):
#     if nums[i]==target:
#         if first==-1:
#             first=i
#         last=i
# print(last, first)


#OPTIMAL
low=0
high=len(nums)-1
lb=-1 
ub=-1
while low<=high:#first occurnace
    mid=(low+high)//2
    if nums[mid]>=target:
 
        high=mid-1
        lb=mid
    else:
        low=mid+1
while low<=high:#last occurance
    mid=(low+high)//2
    if nums[mid]>target:
        
        high=mid-1
        ub=mid
    else:
        low=mid+1
# print(nums[lb],nums[ub-1])
print([-1,-1] if lb==-1 or nums[lb]!=target else lb,ub-1)
#TC--2NlogN, SC--N