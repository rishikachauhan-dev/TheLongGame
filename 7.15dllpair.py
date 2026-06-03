#brute
hashmap=set()
curr=head
result=[]
while curr is not None:
    remain=target-curr.data
    if remain in hashmap:
        result.append([remain,curr.data])
    hashmap.add(curr.data)
    curr=curr.next

return result


left=head
right=head
ans=[]
while right.next is not None:
    right=right.next # at last right will be none  so next loop wil not run cuz its cjeckin if right is not none so chack right.next is none

while left is not None and right is not None and left.data<right.data: # comparing data not nodes
    total=left.data+right.data
    if total==target:
        ans.append([left.data,right.data])# storing val not nodes also in pair[(),()]
        left=left.next
        right=right.prev
    elif total<target:
        left=left.next #left node++
    else:
        right=right.prev #right--
return ans
