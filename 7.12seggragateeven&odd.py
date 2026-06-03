#brute

if head is None or head.next is None:
    return head

stack=[]
temp=head

#stacking odd 1-based indexing values 
while temp :  #same as temp is not None----------o(n/2)
    stack.append(temp.val)
    temp=temp.next.next if temp.next else None # else temp none attribute error


#even
temp=head.next # starting from 2nd index
while temp: # so(n/2)
    stack.append(temp.val) # append val not node imp else out of range
    temp=temp.next.next if temp.next else None

temp=head
index=0
while temp is not None: #o(n)
        temp.val=stack[index]
        index+=1  # this better cuz ll is not index based tho for handle index better
        temp=temp.next
    return head

#o(n) and sc-o(n)


#optimal

if head is None or head.next is None:
        return head
    
    odd=head
    even=head.next
    even_head=even
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    
    odd.next=even_head
    return head
#o(n), sc-o(1)