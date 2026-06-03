#Right rotate array by 1 place
nums=[2,4,1,7,8,9,5,3]
n=len(nums)
temp=nums[n-1]
for i in range(n-2,-1,-1):#(-6,-1, decreas by -1) why 6? cuz i+1
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)