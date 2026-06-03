class ListNode:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev=prev

#optimal--brute same as sll

prev=None
curr=head
while curr is not None:
    front=curr.next
    curr.next=prev # reverse
    curr.prev=front #reverse

    prev=curr
    curr=front
return prev
