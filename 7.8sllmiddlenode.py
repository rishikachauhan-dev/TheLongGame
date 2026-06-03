#return middle node for a given head in LL and if even return second middle

#Brute--count LL
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr is not None:
            count+=1
            curr=curr.next

        curr=head
        mid=count//2 # even if odd or even will give the ans 7//2=3 6//2=3
        for _ in range(0,mid):
            curr=curr.next
        return curr
    

#optimal--o(n/2)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        # while fast!=None or fast.next!=None: #lookups o(1)
        while fast is not None and fast.next is not None: #lookups o(1) better and more relible always check like this
            slow=slow.next
            fast=fast.next.next
        return slow