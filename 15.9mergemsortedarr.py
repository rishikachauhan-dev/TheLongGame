#super brute
'''
Take every value → put into array → sort → create one linked list.
Input data
    ↓
Extract everything
    ↓
Put into array
    ↓
Sort
    ↓
Build desired structure
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]

        # take every node form each ll
        for i in range(len(lists)): #o(k)
            temp=lists[i] # now even i=0 have all values in a LIST not lists cuz ll

            #extract to arr
            while temp: #o(n)
                arr.append(temp.val)
                temp=temp.next

        arr.sort() #o(nlogn)

        #covert to ll
        head=ListNode(arr[i])
        curr=head
        for val in arr[1:]: #o(n*k) # all elements in each lists
            curr.next=ListNode(val) #head.next=val
            curr=curr.next
        return head

#TC- o(nlogn)+o(k)+o(n)=o(nk)
# SC-o(n*k)+o(n)  

#-------------------------------------------------------------------
'''
in place follow merge sort
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head=lists[0]
        for i in range(1,len(lists)): # 0=head
            head=self.mergeList(head,lists[i])
        return head

    def mergeList(self,l1,l2):
        dummy=ListNode(0)
        curr=dummy
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        # end nodes left
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dummy.next
    

#--------------------------MIN HEAP

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i])) #i for diff same index
        dum=ListNode(0)
        temp=dum
        while len(pq)!=0:
            val,i,node=heapq.heappop(pq)# pop the smallest
            temp.next=node # add to the dumm list
            temp=temp.next

            #add next node from the same list to pq
            if node.next:
                heapq.heappush(pq,(node.next.val,i,node.next))
        return dum.next
        
