# UPPER/LOWERBOUND
# | Name            | Meaning                                 | Condition          |
# | --------------- | --------------------------------------- | ------------------ |
# | Lower Bound | First index where target can sit        | nums[i] ≥ target |
# | Upper Bound | First index where target must move past | nums[i] > target |

# [1,1,1,2,2,3,3,3,4,5...]
#           ↑    ↑
#         LB(3)  UB(3) 
# LB(3) = 5 → first 3
# UB(3) = 8 → first value greater than 3 (the 4)

#LowerBound-----------------
#return index of number which is nums[i]>=target basically the lowest value you can get so that its just greater that target
nums=[1,1,1,2,2,3,3,3,4,5,5,6,7,8,9,11,14,15]
target=20
low=0
high=len(nums)-1
temp=0
lb=len(nums) # by defualt if no value present lb=-1 or this if asked what index will be of edge case
while low<=high:
    mid=(low+high)//2
    # print(mid)
    if nums[mid]>=target:
        lb=mid
        high=mid-1 # the difference is here line 26 vs 47 cuz here we want to continue if there are anymore smalest no.?
    else:
        low=mid+1
print(lb)
#TC=o(log2N)

#recursion
# def lowerb(nums,low,high):



##GFG--larget nums[i]<=x
arr= [1, 2, 8, 10, 10, 12, 19]
x = 11
low=0
high=len(arr)-1
lb=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]<=x: #line 45-47 by moving low towards m its checking if there is more num on the rigth of the array and storing it in lb
        lb=mid
        low=mid+1 # but here we want to see if there are any more largest no.
    else:
        high=mid-1
print(lb)

#Naukar360----UpperBound
x= 45
arr=[5,12,12, 15, 18, 21, 35, 37, 38, 46, 47, 48, 48, 50,] 

low=0
high=len(arr)-1
up=len(arr)
while low<=high: # pt equal sign otherwise it exists if its equal--thats the bug
    mid=(low+high)//2
    if arr[mid]>x:
        up=mid
        high=mid-1
    else:
        low=mid+1
print(up)