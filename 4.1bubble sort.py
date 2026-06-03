nums=[5,7,8,4,1,6,9,2]
n=len(nums)
for i in range(n-2,-1,-1):# till -1 index as range is exlusive cuz we wan to include 0
    for j in range(0,i+1):# till i
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)

#Tc-loop i-j---o(n(n+1)/2)--o(n^2) sc-o(1)
