'''
stack pe queue functions-2stack 1 queue
'''
class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[] #helper to be turned to que

    def push(self, x: int) -> None: #pushing for top element and pop first element
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int: # will want to theblast element to pop
        if self.empty():
            return-1
        top=self.stack1.pop()
        return top
        
    def peek(self) -> int: 
        if self.empty():
            return -1
        return self.stack1[-1]
        

    def empty(self) -> bool: 
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
push: O(1)
pop: Amortized O(1) (costly transfers only when out_stack is empty, and each element is moved at most once)
peek: Amortized O(1)
empty: O(1)
Space: O(n), where n = number of queue elements

'''