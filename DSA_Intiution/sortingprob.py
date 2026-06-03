arr=[3,5,7,4]

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1

    while j>=0 and arr[j]>=key: #till j>key shift everything right
        arr[j+1]=arr[j] # shift right
        j-=1 #now this is the pos where j is NOT> key
    arr[j+1]=key
print(arr)
