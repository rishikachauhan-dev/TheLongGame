# 2Sum Problem
'''
brute:
for every i try every j if that equals to target

o(n^2)

optimal:

for i in nums target-num  
if in hashmap return   o(1) lookup
else add to hashmap

o(n)
o(n)
'''
# Kadane's Algorithm, maximum subarray sum

'''
| Type        | Can skip? |
| ----------- | --------- |
| Subarray    | ❌ No      |
| Subsequence | ✅ Yes     |

return the sum of the array that gives the max sum that in can generate

here cant skip middle elements

optimal
maxi=float(-'infi')
for every in nums add to total
and compare with maxi and store it in maxi max(maxi,total)
if total neg reset

'''
# Stock Buy and Sell
'''
what is the min price to buy stack and max price to sell to have max profit?, cant sell backwards

mini=float(infi)
max=0  cux if no profit return 0
for num in nums,
mini=min(mini,num)
profit=num-mini
maxi=(maxi,profit)

o(n)

'''

# Rearrange the array in alternating positive and negative items
'''
brute:
for i in arr if >0 add to pos arr else neg arr
then p  and each add the original arr one by one even and odd index of arr

o(2n)
o(n/2+n/2)

optimal:
newarr=[0]*n
posi, negi= 0,1 of newarr

for num in nums if >0 
add to newarr then [posi]++2
else add to new negi++2

o(n), o(n), this works cuz negative starts from 1 so it will alwaps be in in odd
'''
# Longest Consecutive Sequence in an Array

'''nums=[1,99,101,98,2,5,3,100,1]
brute:
sort nums
count=0
maxi
for i  from 1 til n in nums if nums[i]==nums[i-1]+1 count+2
max(maxi,count)

o(nlogn+n)
o(1)

optimal:
add nums to set
if num-1 not in set, put x=num so that it wont change the original,  o(1) lookups
start counting count++ from x++ till x not in myset

maxi=max(maxi,count)

o(n)
o(1)
'''


# Rotate Matrix by 90 degrees
'''
swap elemets of lower half to upper half, then reverse each element in row
[
123
456
789
]
741
852
963

147 { 1,0-0,1}
258
369 reverse each row elements, low triangle i>j, focus right below, for [i][c],swap till c<i, i++,j++
'''

# Print the matrix in spiral manner

'''
top=0, start row identifier
left=0, start col identifier
bottom=n end row identifier
right=m end col identifier

append it to result, for i in range(left to right,right to bottom, bottom to left, bottom to top)
result.append([i][const at the moment])
'''