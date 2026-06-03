#Architecture
'''
1. get by index
2. add @ head
3. add @ tail
4. add @index
5. delete @index
'''


class Node:

    def __init__(self,val=0,next=None):# the user will use this
        self.val=val
        self.next=next
class MyLL:
    def __init__(self):# here its not inside or like the above class becuz the user doenst need to provide it
        self.head=None #The user should not decide these values.
        self.size=0#So the constructor sets default internal state:

    def get(self,index:int):
        if index<0 or index>=self.size:
            return -1
        #hop
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val

    def addAtHead(self,node):
        node=Node(val,self.head)
        # node.next=self.head # not here bur inside Node()
        self.head=node# current self.head will be the new node
        self.size+=1

    def addAtTail(self, node):
        node=Node(val) #since it will be last no need to think abt address
        #edge case
        if not self.head:
            self.head=node
        else:
            curr=self.head
            while curr is not None:
                curr=curr.next
            curr.next=node # this will be the empty emory after the curr node that has none as an address

    def addAtindex(self,index,node):
        if index<0 or index>=self.size:
            return 'out of bounds'
        if index==0:
            self.size==1:
            self.addAtHead(node)
        else:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next# is @2 for eg. if we want to insert @3
            node=Node(val,curr.next) #the address stored in 2 so that it points to 3 so curr points at val 2 the address is curr.next
            curr.next=node # the value of curr.next was 3 so we insert our value
            self.size+=1
    def delAtindex(self,index,node):
        if index<0 or index>=self.size:
            return 'out of bounds'
        if index==0:
            self.head=self.head.next
        for _ in range(index-1):
            curr=curr.next# curr @value 2 delete 3
        curr.next=curr.next.next #value of 3 replaced by 4
        
        