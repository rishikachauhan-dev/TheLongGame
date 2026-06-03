# Structure of linked list Node
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top=None
        
    def isEmpty(self):
        # Check if the stack is empty
        return self.top is None

    def push(self, x):
        # Adds element x to the top of the stack
        # create new node
        new_node = Node(x)

        # new node points to old top--pointig downwards
        new_node.next = self.top

        # move top to new node
        self.top = new_node
            
        
    def pop(self):
        # Removes an element from the top of the stack
        if self.top is None:
            return -1
            
        popped=self.top.data
        
         # move top downward
        self.top=self.top.next #points to old top next is the old one
        return popped
        
    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.top is None:
            return -1
        return self.top.data
        
    def size(self):
        # Returns the current size of the stack
        count=0 #len is fucnt
        curr=self.top
        while curr:
            count+=1
            curr=curr.next
        return count
    


################
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.front=None
        self.rear=None

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.size()==0

    def enqueue(self, x):
        # Add element x to the rear
        #creating node
        new_data=Node(x)
        #1 empty
        if self.rear is None:
            self.front=self.rear=new_data
            return # else below code will run unnecessarily
        #2 already exists
        self.rear.next=new_data #move reaqr to next it will be None now
        #adding to LL
        self.rear=new_data
        
    def dequeue(self):
        # Remove the front element
        if self.front is None:
            return -1
        popped=self.front.data
        self.front=self.front.next #move front to next pointer
        
        #if it become emty after pop
        if self.front is None:
            self.rear=None
        return popped

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.isEmpty():
            return -1
        return self.front.data


    def size(self):
        # Return current size
        count=0
        curr=self.front
        while curr:
            count+=1
            curr=curr.next
        return count
            