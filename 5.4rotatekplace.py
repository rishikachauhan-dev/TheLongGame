#My code
nums=[1,2,5,6,8,4]
k=3
n=len(nums)
j=0
while j<k:#if k=3, the j=0,1,2
        temp=nums[n-1]#1 not n-j cuz after line 10 the element at new list will be at last
        for i in range(n-2,-1,-1):
            nums[i+1]=nums[i]
        nums[0]=temp
        j+=1  
print(nums)

#Tc=kxn  Sc=o(1)


#Brute force
nums=[4,5,6,8]
n=len(nums)
k=13
#optimizations
roations=k%n # for if len=6 then rotation 1,2,3,4,5,6 at six it will be same like the original after the if its a multiple of six it will repeat the same
for _ in range(0,k): #o(k)
      poped=nums.pop()
      nums.insert(0,poped) # insert at 0 indx #o(n) cux if inserted automatically all elments wil move to right
print(nums)

#Tc=o(kxn)-for k loop k times then nums insert for each k each element n times shift

#Better solution slicing
nums=[4,5,6,8]
n=len(nums)
k=k%n #2
#slicing:indx 0,1, 2,3-
#            6,8  4,5   
nums[:]=nums[n-k:]+nums[:n-k] #nums[n-k:]=o(k) will slice, nums[:n-k]=0(n-k) will slice
print(nums)
#Tc=o(k+n-k)=o(n) Sc=o(1)
#Python slicing is start inclusive, end exclusive.
#Why nums[:] = instead of nums = ?--fisrt one modifies the same list other makes a new list

#optimal solution:
nums=[3,9,5,6,7,8,9]
k=4
n=len(nums)
def reverse(nums,i,j):
    while i<j:
        nums[i],nums[j]=nums[j],nums[i] #Swap
        i+=1
        j-=1
reverse(nums,n-k,n-1) # reverse k elements Tc=k/2
reverse(nums,0,n-k-1)# reverse starting elements Tc=(n-k)/2
reverse(nums,0,n-1) #Tc=n/2
print(nums)

#Tc=o(n)


     
