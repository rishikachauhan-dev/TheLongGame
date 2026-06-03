#for rect node
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None


class singlyLikedList:
    def __init__(self):# init--the blue print the func inside it
        # if no node is added by defualt head=none
        self.head=None # we need to create a head to know the starting point tpp
# case 1- list already there--how to append it?-- append=add last element to list
    def append(self,val):
        new_node=Node(val)  
        if self.head==None:
            self.head=new_node # now change this to new node if thers no head--edge case 2- if list empty
        else:
            curr=self.head # start from head to find the last element
            while curr.next is not None: # cuz last element has none as the nex address
                curr=curr.next #the adress of the new val so that it is not none
            curr.next=new_node # type: ignore # the val
# Tc-o(n), Sc=o(1) cuz no extra memory created

#now to print the list--
#traverse
    def traverse(self):
        if self.head is None:
            print('SLL is empty')
        else:
            curr=self.head
            while curr is not None:
                print(curr.val, end=' ')# space for the output
                curr=curr.next
            print()
sll=singlyLikedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(50)
sll.append(60)
sll.traverse()

# curr.next?
#---to call next outside the Node class

# | Where you are | What to use             |
# | ------------- | ----------------------- |
# | Inside class  | `self.attribute`        |
# | Outside class | `object_name.attribute` |
