#Brute

#DLL
#edge cases if starting values are key change head and if ll contains on key return none

if head is None:
    return None

curr=head
while curr is not None:
    if curr.val==key:

        #if deleting head
        if curr.prev is None : #checking if its really head
            head=curr.next #change head
            if head is not None:
                head.prev=None #backward link to previous after changing head

        else: # some middle values
            #curr is the one to be del
    
            curr.prev.next=curr.next #forward link
            if curr.next is not None: # cant create backward link if its None
                curr.next.prev=curr.prev #backward link

    curr=curr.next
return head

## bug---curr.prev.next=curr.next #forward link earlier curr.prev=curr.next #forward link
#now works

#o(n), sc-o(1)


#passes all the test cases--
curr = head
prev = None
new_head = head

while curr is not None:
    if curr.data == x:
        if prev is not None:
            prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = prev
        if curr == new_head:
            new_head = curr.next
    else:
        prev = curr
    
    curr = curr.next

return new_head
