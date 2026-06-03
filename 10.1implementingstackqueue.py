#LIFO
class myStack:
    def __init__(self,n):
        # Define Data Structures
        self.arr=[]
        self.n=n
    
    def isEmpty(self):
        # Check if stack is empty
        if len(self.arr)==0: # len tc: o(1)everytime
            return True
        else:
            return False
            #T/F
    
    def isFull(self):
        # Check if stack is full
        return len(self.arr)==self.n
    
    def push(self, x):
        # Insert x at the top of the stack
        if len(self.arr)!=self.n: #apeending always at last o(1)
            self.arr.append(x)
        else:
            return -1

    
    def pop(self):
        # Removes an element from the top of the stack
        if len(self.arr)!=0:
            return self.arr.pop() #o(1)
        else:
            return -1

    
    def peek(self):
        # Returns the top element of the stack
        if len(self.arr)!=0:
            return self.arr[-1]
        else:
            return -1
        
# all o(1)

###############################################

#FIFO
#    
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.arr=[]
        self.n=n
    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.arr)==0
        
    
    def isFull(self):
        # Check if queue is full
        return len(self.arr)==self.n

    def enqueue(self, x):
        # Enqueue
        # if len(self.arr)!=self.n:
        return self.arr.append(x)
        
    
    def dequeue(self):
        # Dequeue
        if len(self.arr)==0:
            return
        x=self.arr.pop(0) #o(n)
        return x
        
    def getFront(self):
        # Get front element
        if len(self.arr)!=0:
            return self.arr[0]
        else:
            return -1
    
    def getRear(self):
        # Get rear element
        if len(self.arr)!=0:
            return self.arr[-1]
        else:
            return -1
        

# all o(1) only pop o(n)
#to make pop o(1)
class MyQueue:
    def __init__(self):
        self.arr = [0] * 100005  # Fixed-size array
        self.front = 0            # Pointer to front
        self.rear = 0             # Pointer to next empty spot at rear
    
    # Function to push an element x in a queue.
    def push(self, x):
        self.arr[self.rear] = x   # Place at rear
        self.rear += 1            # Move rear forward

    '''
    Pop(): If front == rear (empty), return -1. Else, get arr[front], increment front, and return it (remove from start).
    '''
    
    # Function to pop an element from queue and return that element.
    def pop(self):
        if self.front == self.rear:
            return -1             # Queue empty
        temp = self.arr[self.front]  # Get front element, temp=0 index, now make the front from 0, return temp, popped
        self.front += 1           # Move front forward, front = front + 1 update it
        return temp
    '''basically we have to return the front element after popping put the actual front in temp then move the self.front to the next element to start the queue'''