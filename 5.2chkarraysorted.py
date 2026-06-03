# Return bool
arr=[1,4,5,6,2,8,9,12]
def sort(arr):
    for i in range(0,len(arr)):
        if arr[i]>arr[i+1]:
            return False
    return True
print(sort(arr))

#Tc=o(n) Sc=o(1)