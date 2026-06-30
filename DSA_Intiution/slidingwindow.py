# Longest Substring Without Repeating Characters
'''
s = "pwwkew"
s="abcabcbb"
l=0
r=0
set={}
while r<len(s):
    if s[r] in set:
        #update that value with curr index and increment l to +1 in set
        
        l=max(l,set[s[r]]+1)
        
    maxi=max(maxi,r-l+1)
    set[s[r]]=r #assign curr index
    r+1
return 

'''
# Max Consecutive Ones II
'''max allowed to to flip=1
so for right in len(nums)
    zeroes+=nums[right]^1:
    if zeroes>1:
        zeroes-=nums[left]^1 # basically where it is one so when left reaches that index
        left+=1, till zeroes remain >1
    now ans=(ans,right-left+1)
        '''
# o(1)-2 pointers
# III
'''
same but zeroes>k

n=len(nums)
right=0
left=0
maxi=0
zeroes=0
for right in range(len(nums)):
    zeroes+=nums[rigth]^1
    if zeroes>k:
        zeroes-=nums[left]^1
        left+=1
    maxi=max(maxi,right-left+1)

print(maxi)
'''

# Fruit Into Baskets

'''make a dict and increase the count +1 of the same no. if the len(dic)> 2
left+1 till dict[key]==0, then del that key
stare that in ans return max ans, right-left +1 : right, left indexes of the fruits and the cond is contigous array-subarray'''
# Maximum point you can obtain from cards
'''left and right at opp ends, left++ add that till cards can pick, then right--, left-=1 add to sum

2 for loop-one to add left till cards pick, then maxi =sum of cards,
right for loop to add right and decrement left'''