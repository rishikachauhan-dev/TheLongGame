#queue pe stack functions-2queue, 1stack, dequeue-popleft and rotate

'''
implement working of basic functions of stack, in queue

originaly:
stack=[1,2,3,4] top=4, pop=4, after push(4)
queue=[1,2,3,4] top/front=1,pop/deque=1, push/enque=4

so after this
when queue front=4, pop=4


basic approach is for pop and push to get the first element in o(1) by here since queue it will be o(n)

'''

from collections import deque
'''Depending on your language, the queue may not be supported natively(not in python). You may simulate a queue using a list or deque (double-ended queue) as'''
class MyStack:

    def __init__(self):
        self.q=deque()
        #deque here acts as a container only

    def push(self, x: int) -> None:
        #first enque
        self.q.append(x)

        for _ in range(len(self.q)-1): #rotating old elements
            val=self.q.popleft()# pop at 0
            self.q.append(val) #append at last till n-1 so that new elemts comes first

    def pop(self) -> int:
        # if empty?
        # if len(self.q)==0: #o(1)
        #     return -1
        if self.empty():
            return -1
        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            return -1
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0

'''1stack, 1dequeue where rotate after push from 0 index ie. popleft
'''


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
maintain q1 as the “stack” where the front is the top. 
During push, we use q2 to temporarily hold the new element, then pour q1 into q2 (which puts old elements behind the new one). 
Swapping makes q1 the updated queue with new top at front.

'''
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
    
    def push(self, x: int) -> None:
        self.q2.append(x)  # Add new element to helper
        # Move all from main to helper
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap: helper becomes main
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self) -> int:
        return self.q1.popleft()  # Remove front (top of stack)
    
    def top(self) -> int:
        return self.q1[0]  # Peek front
    
    def empty(self) -> bool:
        return len(self.q1) == 0  # Check if main is empty
    
#o(n)-push, o(n)
'''
2queue
q1 and q2 popping from s1 will make the s2 have the bottom element at top so swap s2 to make it main'''