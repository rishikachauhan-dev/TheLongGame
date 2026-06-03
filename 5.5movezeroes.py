nums = [0,1,0,3,12]
n=len(nums)

#Mycode
for i in range(0,n-1):
    if nums[i]==0: #o(n)
        nums[i],nums[i+1]=nums[i+1],nums[i]# Swap
    if nums[i-1]==0:#o(n)
        nums[i],nums[i-1]=nums[i-1],nums[i] 
        i-=1
    i+=1
print(nums)
#Tc=o(2n)=n Sc=o(1)
#3rd testcase failed so better

#---------------

#Brute
temp=[]
for i in range(len(nums)): #o(n)
    if nums[i]!=0:
        temp.append(nums[i])
    #now putting it in nums
nz=len(temp)
for i in range(0,nz): #n/2
    nums[i]=temp[i]#the list will look--[1,3,12,3,12]
for i in range(nz,n): #n/2
    nums[i]=0
#Tc=o(2n) sc=o(n)



#---------------
#Optimal
#2 pointer approach
nums = [0,1,0,3,5]
n = len(nums)
j = 0  # pointer for position of next non-zero element
for i in range(0,n): #0,1,2,3,4
    if nums[i] != 0:# skip,1,skip,3,5
        nums[i], nums[j] = nums[j], nums[i] #[1,0,0,3,5]..[1,3,0,0,5]..[1,3,5,0,0]
        j += 1 #1, 2
print(nums)


