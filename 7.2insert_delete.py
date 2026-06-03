#inserting gfg
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution1:
    def insertAtEnd(self, head, x):
        #code here 
        new_node=Node(x)
        if head==None:
            head=new_node
        else:
            curr=head # dont use self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
        return head


#leetcode
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy value from next node
        node.val = node.next.val
        # Skip next node
        node.next = node.next.next

#TC=o(1), Sc=o(1)
# logic:
