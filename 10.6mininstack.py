#wrong code
class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('infinity')
        

    def push(self, val: int) -> None:
        self.mini=min(val,self.mini)
        self.stack.append(val)
        

    def pop(self) -> None:
        p=self.stack.pop()
        return p
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #update min in each pop? but o(1) cuz pop o(1)
        ''' mini=min(e=stack2.pop().mini till epmty? but copy a stack-o(1)?-no)
        mini=min(e=pushed element,mini) but this in pushed function
        '''
        return self.mini
    '''Your logic is incomplete ❌
    Main issue:
    self.mini
    only updates during PUSH.
    But when minimum element gets popped:
    mini becomes outdated 😭'''

    # idea is to get min in current
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#------------------------------------------------------------
class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append([val,val]) #([val,min])([0,1])but since empty curr is min
        else:
            mini=min(self.stack[-1][1],val)#([top,at 1 index in the list]),curr val
            self.stack.append([val,mini])


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack)==0:
            return 0
        else:
            return self.stack[-1][0] #top at 0 index
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()