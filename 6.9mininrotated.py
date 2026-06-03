#Find min in rotated array
nums=[4,5,6,7,0,1,2]
# need to 0

#Brute:
mini=float('infinity')
for i in range(len(nums)):
    mini=min(nums[i],mini)
print(mini)

#Tc=o(n), SC=o(1)

#Optimal logn
low=0
high=len(nums)-1
mins=float('infinity')
while low<=high:
    mid=(low+high)//2
    #checking left arr
    if nums[low]<=nums[mid]:
        mins=min(nums[low],mins)
        low=mid+1 #else move to other side # for nums it gets sorted is here itself no need for else loop
    else: # checking right array
        if nums[mid]<=nums[high]:
            mins=min(nums[mid],mins)
            high=mid-1
print(mins)
    
