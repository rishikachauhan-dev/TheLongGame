arr= [1, 1, 2, 2, 2, 2, 3, 3,5,6]
arr= [1, 1, 2, 2, 2, 2, 4,5,6]
target = 3

#Brute

def countFreq(self, arr, target):
    # code here
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==target:
            if first==-1:
                first=i
            last=i

    if first==-1:
        return 0
    else:
        return (last-first)+1
    #Tc= o(n), Sc=o(1)
        
#OPTIMAL
class Solution:
    def countFreq(self, arr, target):
        # code here
        def lb(arr, target):
            low=0
            high=len(arr)-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>=target: #2 at 2
                    high=mid-1
                    first=mid
                else:
                    low=mid+1
            return first
        def upper(arr, target):
            low=0
            high=len(arr)-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>target:
                    high=mid-1
                    last=mid
                else:
                    low=mid+1
            return last
        f=lb(arr,target)
        if f==-1 or arr[f]!=target: # target not exist
            return 0
        l=upper(arr,target)   # [2,2,2,2,2] edge case
        if l==-1:
            return len(arr)-f
        else:
            return l-f
# one edge case no array

