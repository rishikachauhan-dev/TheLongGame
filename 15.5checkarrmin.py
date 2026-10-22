arr=[4,6,9,12,16,13,19,21]
n=len(arr)
for i in range(n//2 -1,-1,-1):
    lech=2*i+1
    rech=2*i+2
    if lech<n and arr[lech]<arr[i]:
        return False
    if rech<n and arr[rech]<arr[i]:
        return False
return True
