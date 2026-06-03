## Rightmost set bit unset--from above--------------------------

# unset ko set by OR?

if n & (n+1)==0:
    return (n<<1) | 1
else:
    return n| (n+1)


## BIT FLIPS---------------
#Tc-o(32), SC-o(1)

"""function countBits(start, goal):

    temp = start XOR goal
    count = 0

    while temp > 0:
        if last bit of temp is 1:
            increase count

        shift temp right by 1

    return count"""

temp=start^goal
count=0
while temp>0:
    if temp & 1: #==1: no need for this line
        count+=1
    temp>>1
return count

#but this TLE
" so line---temp = temp & (temp - 1): removes 1 each time"




#Single no.---------------
#Tc-o(n), Sc-(1)
ans=0
for i in nums:
    ans=i^ans
return ans