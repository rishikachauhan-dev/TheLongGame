nums=[3,5,6,4,8,9,10,7,1]
n=len(nums)
for i in range(1,n):#0 index sorted and cant compare w/-1\\ 5
    key=nums[i]#5
    j=i-1# to compare previous one \\ 3
    while j>=0 and nums[j]>key: # start from 0 index and if value at j is > key\\3>5?
        nums[j+1]=nums[j]#at index of 4 replace 6 (that is j)
        j-=1# if the previous is >
    nums[j+1]=key #// key this will replace 

print(nums)

## in for loop but while better cuz shorter and in if need to break it
nums=[8,6,2,4,7,10,1]
n=len(nums)
for i in range(1, n):
    key = nums[i]
    for j in range(i-1, -2, -1):   # i-1 down to 0 stop till -2 not -1 cuz 
        if nums[j] > key:
            nums[j+1] = nums[j]    # shift right
        else:
            break
    nums[j+1] = key                # place key

print(nums)