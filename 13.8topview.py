class Solution:
    def topView(self, root):
        # code here
        if not root:
            return None
        ans=[]
        result={}
        queue=deque() #will unpack so not the usual way in ques
        # queue=deque([root,0]) #cant unpack this way do queue=deque([(root,0)]) we need this in a tuple
        queue.append((root,0))
    
        while queue:
            # for e,line in range(len(queue)): no this
                e,line=queue.popleft() #unpack this wat
                if line not in result: #searching for the index no the value # this is the line to check it is for the first time
                    result[line]=e.data
                if e.left:
                    queue.append((e.left,line-1))
                if e.right:
                    queue.append((e.right,line+1))
                    
        for values in sorted(result.items()): #no need for len cuz its n in nums
            ans.append(values[1]) #1 for the index in the tuples the root data is in the 1 index
        return ans
#o(n+nlogn+n)-while, sort, ans append, o(n+n)-queue, result, ans-no need cuz we return it

'''
add all to queue then pop and check if already in result? the fisrt value will be the leftmost or the right most

since 0 for root, left line-1, right line+1
'''
'''easy to remebr way'''
# for key, value in sorted(hash.items()):
#                 result.append(value) #index of the list 'key-value'
#             return result

# sorted(result.items()): this always retuen a tuple and is how u sort a dict

#w/ HELPER FUNC----------------------------------------------

from collections import deque
class Solution:
            
        def bfs(self,node):
            que=deque([(node,0)]) # a list in the queue (kind of a lIFO stack)
            #([()]) to create a tuple else non iterable
        
            while que:
                # for _ in range(len(que)): dont need this line not seeing levels
                e,ind=que.popleft()#unpack [root,0] [e,ind]
                if ind not in self.hash: # check?
                    self.hash[ind]=e.data
                if e.left:
                    que.append([e.left,ind-1])
                if e.right:
                    que.append([e.right,ind+1])
                    
        def topView(self, root):
        
            if not root:
                return []
            self.result=[]
            self.hash={}
            self.bfs(root)
            #sort cuz thats the out req so most neg ind will come first
            for key, value in sorted(self.hash.items()):
                self.result.append(value) #index of the list 'key-value'
            return self.result