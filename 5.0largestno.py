#M-1
# find the largest no. in an array

arr=[55,32,-96,99,3]
largest=arr[0]# assuming this is the largest
for i in range(0,len(arr)):
    largest=max(largest,arr[i])
    print(largest)
print(f'Final-{largest}')
# max wont matter cuz same complexity

#if
arr=[2,22,-96,-99,38]
largest=float('-infinity')
for i in range(0,len(arr)):
    if largest<arr[i]:
        largest=arr[i] # tc-o(1) cuz comparing only 2 var.
    print(largest)
print(f'Final-{largest}')


#TC=o(n) sc=o(1){spce is const}