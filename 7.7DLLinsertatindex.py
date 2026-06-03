
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


#IN Ques the we have to insert AFTER p
class Solution:
    def insertAtPos(self, head, p, x): 
        new_node=Node(x)
        curr=head 
        for _ in range(p): 
            # while curr: no need for this overshot
            curr=curr.next
        
        #all bout new node fist all things on new node
        #pehle bich mei bithao iska connet kr k
        new_node.next=curr.next# this handles none if the
        #next is not but none doesnt have prev so will give error so will check for only none-prev cond
        new_node.prev=curr 
        
        if curr.next:
            curr.next.prev=new_node
        curr.next=new_node
        # curr.next=new_node # address 2->new # always at last
        return head
        
        '''
        99.next = 3
        99.prev = 2
        
        3.prev = 99
        
        2.next = 99
        '''
            
        