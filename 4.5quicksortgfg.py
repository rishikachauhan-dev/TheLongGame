#pivot=last element

##WRONG CODE DONT IMPLEMENT

arr=[9,1,4,2]
def quickSort( arr, low, high):
    if low<high:
        pindex=partition(arr, low, high)
        quickSort( arr, low,pindex-1)
        quickSort( arr, pindex+1,high)

def partition(arr, low, high): #arr=[9,1,4,2] 9=low pivot=2  high=2,4
    pivot=arr[high]#4
    i=low-1 # So:i = low - 1 → “no spots reserved yet”.
            #i = low → “I already reserved a spot”, which is wrong at the start.
    # print(arr[i])
    j=high
    while arr[i]<=pivot and i<=high-1:
        i+=1# 0,9 0,2 1,1
    while arr[j]>=pivot and j>low:
        j-=1#2,4,1
    if i<j:
        arr[i],arr[j]=arr[j],arr[i]#9-2
    arr[high],arr[i]=arr[i],arr[high]#high 4 [2,1,4,9]
    return i
quickSort(arr,0,len(arr)-1)
print(arr)


#correct code

arr = [9,1,4,2]

def quickSort1(arr, low, high):
    if low < high:
        pindex = partition1(arr, low, high)
        quickSort1(arr, low, pindex-1)
        quickSort1(arr, pindex+1, high)

def partition1(arr, low, high):
    pivot = arr[high]     # choose last element as pivot
    i = low - 1

    for j in range(low, high): #j=till high-1 here
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


quickSort1(arr, 0, len(arr)-1)
print(arr)