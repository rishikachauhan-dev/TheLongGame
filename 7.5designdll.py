class Node:
    def __init__(self,prev=None,val=0,next=None):
        self.prev=prev
        self.val=val
        self.next=next

class MyDLL:
    def __init__(self):
        self.head=None
        self.size=0

    def get(self,index):
        if index<0 or index>self.size:
            return 'out of bounds'
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val
    
    def insertAthead(self,node):
        node=Node(None, val, self.head)
          # but connect the previosn head to the new head
        if self.head:
            self.head.prev=node
        self.head=node
        self.size+=1

    def insertAttail(self):
        node = Node(None, val, None)
        # edge case
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            node.prev = curr
            curr.next = node
        self.size += 1

    def insertAtindex(self,index,node):
        if index<0 or index>=self.size:
            return -1
        if index==0:
            return self.insertAthead(node)
        curr=self.head
        for _ in range(index-1): #insert b/w 2 and 3
            curr=curr.next
        node=Node(curr,val,curr.next)#(2,34,3)
        if curr.next:
            curr.next.prev=node #3 previous needs to connect to node but what if not there?
        curr.next=node #after 2=new node
        self.size+=1

    """def delete(self,index):
        if index<0 or index>=self.size:
            return -1
        if index==0:
            self.head=self.head.next
            self.head.prev=None
        curr=self.head
        for _ in range(index-1): # 2-4 want to delete 3
            curr=curr.next # curr=2
        # node to delete curr.next
        if curr.next.next: # will check if its none or not cuz none.prev doesnt make sence if theres no node.
            curr.next.next.prev=curr #2<-4 # what if its at last?
        curr.next=curr.next.next # 2->4 # value of 3 replace by 4
        
        self.size-=1
        """  # Here deleting head will stuck in a loop

def delete(self, index):
    if index < 0 or index >= self.size:
        return -1

    # delete head
    if index == 0:
        self.head = self.head.next
        if self.head:
            self.head.prev = None 
        self.size -= 1 
        return

    curr = self.head
    for _ in range(index - 1):
        curr = curr.next

    # node to delete = curr.next

    if curr.next:  # safety
        if curr.next.next:
            curr.next.next.prev = curr

        curr.next = curr.next.next

    self.size -= 1


#gfg ques--
    '''def delPos(self, head, x):
        if not head: # list empty?
            return 
            
        if x==1:
            head=head.next
            if head: # backward link but what if head.next is None only 1 LL
                head.prev=None
            return head # here too if ir will be 1 digit
        
        curr=head
        for _ in range(x-2): # one before
            if curr is None or curr.next is None: # out of bounds
                return head
            curr=curr.next
            
        if curr.next: # what if it is
            curr.next=curr.next.next
            if curr.next.next:
                curr.next.next.prev=curr
             
        return head'''
    class Solution:
    def delPos(self, head, x):
        if not head: # list empty?
            return 
            
        if x == 1:
            head = head.next
            if head:
                head.prev = None 
            return head

        curr = head
        for _ in range(x - 2):
            #out of bounds pos
            if curr is None or curr.next is None:
                return head
            
            curr = curr.next
    
        # node to delete = curr.next
    
        if curr.next:  # safety
            if curr.next.next:
                curr.next.next.prev = curr #backward link
    
            curr.next = curr.next.next # forward link
            
        return head