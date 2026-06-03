# idea behind SLL

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None # for last one it'll be none

node1=Node(5) # savinf the address of it
node2=Node(6)
node3=Node(9)
node4=Node(11)

node1.next=node2 # type: ignore
node2.next=node3 # type: ignore
node3.next=node4 # type: ignore


print(node1)# it'll be an object
print(node1.val)# it'll be an object
print(node1.next.next)
print(node1.next.next.next.val)


#but this not efficient cuz how many node will you make?