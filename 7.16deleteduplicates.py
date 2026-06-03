#duplicate

#o(n)

curr=head
while curr is not None:
    if curr.data==curr.prev.data:
        if curr.prev==head:
            head=curr
            curr.prev=None
    #forward link
        curr.prev.prev.next=curr
        #backward link
        curr.prev=curr.prev.prev
    curr=curr.next
return head

#DEBUGGED
def removeDuplicates(self, head):
    curr = head
    
    while curr is not None:
        if curr.prev and curr.data == curr.prev.data: # if curr.prev is not None and 
            prev = curr.prev   # node to delete #assigning prev
            
            # if prev is head → update head
            if prev == head:
                head = curr
                curr.prev = None
            else:
                # connect prev.prev to curr
                prev.prev.next = curr
                curr.prev = prev.prev
        
        curr = curr.next
    
    return head

#BETTER WAY
curr = head

while curr and curr.next:
    if curr.data == curr.next.data:
        # delete curr.next
        curr.next = curr.next.next
        
        if curr.next:
            curr.next.prev = curr
    else:
        curr = curr.next

return head