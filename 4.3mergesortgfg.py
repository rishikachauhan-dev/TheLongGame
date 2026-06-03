nums=[4,1,3,9,7]
l=0
r=len(nums)

def mergeSort(arr,l,r): # backtracking, l=0,4=7\\l=1 r=2
    if l>=r: #0<5
        return
    m=(l+r)//2 # 0+5=5//2=2\\2
    mergeSort(arr,l,m) #0-2=[4,1,3]\\[4] i
    mergeSort(arr,m+1,r)#3-5=[9,7]\\[1] j
    merge(arr,l,m,r) # can put return in front too


def merge(arr,l,m,r):
    left=arr[l:m]
    right=arr[m:r+1]
    i,j=0,0
    k=l# starting index 
    while i <len(left) and j<len(right):
        if left[i]<=right[j]:
           arr[k]=left[i]
           i+=1 # loop ends increment
        else:
            arr[k]=right[j]
            j+=1 # increment
        k+=1
        # left overs
    while i<len(left):
        arr[k]=left[i]
        i+=1# inside so that it increments till loop finishes
        k+=1  
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
mergeSort(nums,0,len(nums)-1)
print(nums)

# indentation error left over while
#base case compare error
