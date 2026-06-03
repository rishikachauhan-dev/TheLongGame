#2nd largest no:

#Brute force
arr=[55,67,2,45,-99,98]
arr.sort()
n=len(arr)
print(arr[n-2])
print(arr)

#Tc=o(nlogN) cuz sorting Sc=o(1)

#better
arr=[5,61,23,55,-29,48]
large=float('-infinity')
s_large=float('-infinity')
for i in range(0,len(arr)):
    large=max(large,arr[i])
for i in range(0,len(arr)):
    if s_large<arr[i] and arr[i]!=large:
        s_large=arr[i]
print(s_large)

#Tc=o(n+n)=o(2n)~o(n) Sc=o(1)

#optimal: in one pass 
# same way but simultanously update bith in one loop

arr=[55,67,2,-29,48]
large=float('-infinity')
s_large=float('-infinity')
for i in range(0,len(arr)):
    if arr[i]>large:
        s_large=large
        large=arr[i]
       
    elif arr[i]>s_large and arr[i]!=large:
        s_large=arr[i]
print(s_large)


#TC=o(n) Sc=o(1)