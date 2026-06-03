#ceil--ceiling smallest no. in the array >=target
#floor--largest no. <=target
n=6
x=5
a=[3, 4, 7, 8, 8, 10]
low=0
high=n-1
ceil=-1 # edge case if not there
floor=-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==x:
        floor=a[mid]
        ceil=a[mid]
        break # need to break the loop if found
    elif a[mid]>=x:
        ceil=a[mid]
        high=mid-1
    else:
        floor=a[mid]
        low=mid+1
print(ceil, floor)

        