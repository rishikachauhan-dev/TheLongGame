class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        curr = head
        
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            
            curr.next = new_node
            new_node.prev = curr
            
            curr = new_node
        
        return head


#insert in b/w


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None



class Solution:
    def insertAtPos(self, head, p, x):
        curr=head
        for _ in range(p-1):
            if curr.next is None:
                break
            curr=curr.next #curr=2
            
        new_node=Node(x)
        
        new_node.prev=curr #here 2<-new
        new_node.next=curr.next # val
        
        if curr.next:
            curr.next.prev=new_node #new<-3
        
        curr.next=new_node # address 2->new # always at last
        return head
            
        