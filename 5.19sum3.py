arr=[-1,0,1,2,-1,-4]# Ques 3 seq whose sum is 0 can be any order but not repeated element and order too--unique
##BRUTE force--3 pointers
my_set=set()
for i in range(len(arr)):
    for j in range(i+1,len(arr)): # no index error??--range(n, n) → empty basically if it reaches n then inner loops nver run | Index error only--index >= len(arr)
        for k in range(j+1, len(arr)): # all this o(n^3) loop k andr loop adds ^
            if arr[i]+arr[j]+arr[k]==0:
                temp=[arr[i],arr[j],arr[k]]
                temp.sort() # not much cuz only 3 elements can ignore nlogn
                my_set.add(tuple(temp))# cant put it as list will give type error! lol true #sc-o(no. of triplets in set that are unique)
print([list(ans) for ans in my_set]) # if this over all list but output we want as each set as list, ## without squre bracket in comprehenisons the putput wull give the dtype--generator object expression

#TC=o(n^3)

nums=[-1,0,1,2,-1,-4]#
##BETTER--atleast n^3 to n^2 --eleminate k
result= set()
for i in range (len(nums)):
    myset=set()#temo set to store third element 
    for j in range(i+1,len(nums)):
        third=-(nums[i]+nums[j])
        if third in myset:
            temp=[nums[i],nums[j],third]
            temp.sort() 
            result.add(tuple(temp))
        myset.add(nums[j])
print([list(ans) for ans in result])
    #Tc-o(n^2)+Sc-o(n)--temp set+result--o(triplets )


#Optimal--cant reduce time complexity so will reduce space complexity
ans=[]
nums.sort()
for i in range(len(nums)):
    # skip duplicate fixed elements
    if i!=0 and nums[i]==nums[i-1]:
        continue

    j=i+1
    k=len(nums)-1
    
    while j<k:
        total_sum=nums[i]+nums[j]+nums[k]
        if total_sum<0:
            j+=1
        elif total_sum>0:
            k-=1
        else:
            temp=[nums[i], nums[j],nums[k]] #already sorted
            ans.append(temp)

            
            # set up the two pointers
            j+=1
            k-=1

            #skip if equal to previous
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1
    print(ans)


