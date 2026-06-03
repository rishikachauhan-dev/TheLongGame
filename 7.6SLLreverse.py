
#Brute--can do it will run but not recommended as its not an actual reverse
stack=[]

#storing
temp=self.head
while temp is not None:
    stack.append(temp.val)
    temp=temp.next

#appending--move temp tp start of the SLL again
temp=self.head
while temp is not None:
    e=stack.pop()
    temp.val=e
    temp=temp.next
return head

#optimal--
  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr is not None:
            front=curr.next #curr.next points to front
            curr.next=prev #curr.next points to prev
            
            prev=curr # move prev to curr
            curr=front # now move curr to front : loops till curr==None
        return prev