#sort distinct vales in place(inside arr)
#Brute
arr=[1,1,3,3,5,23,5,6,7,8,99,99,99] # works for all cases
temp={}
for i in range(0,len(arr)): #o(n)
    if arr[i] in temp:
        temp[arr[i]]+=1 
    else:
        temp[arr[i]]=1
# arr=list(temp.keys()) 
# print(arr)

#tc=o(2n)=o(n)

#line 9 
count=0
for k in temp: # use to get key in dict
    arr[i]=k
    count+=1
print(count)


#Optimal # for this to work random vale cant be in between duplicates
arr=[1,1,3,3,5,5,23,6,7,8,99,99,99]
n=len(arr)
if n==1:
    print(1)
i=0
j=i+1
while j<n:
    if arr[j]!=arr[i]:
        i+=1# next duplicate value of i swap with j
        arr[i],arr[j]=arr[j],arr[i]
    j+=1
print(i+1)

#TC=o(n)

