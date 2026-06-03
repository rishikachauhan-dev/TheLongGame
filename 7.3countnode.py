# Given head of a singly linked list. 
# The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Solution:
    def getCount(self, head):
        # code here
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next
        return count


#find key==smth
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution1:
    def searchKey(self, head, key):
        #Code here
        curr=head
        while curr is not None:
            if curr.data==key:
                return True
                break
            else:
                return False
            curr=curr.next

#better way to write
class Solution2:
    def searchKey(self, head, key):
        curr = head
        
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
            
        return False