class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return None
        ans=[]
        result={}
        queue=deque([(root,0)])
        while queue:
            # e,line in queue: #unpack
            e,line = queue.popleft() #unpack
            # e=queue.popleft() not this way
            result[line]=e.data # the value forgot to use .val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1)) #double brackets cuz recursion call will not work
        for values in sorted(result.items()):
            ans.append(values[1])
        return ans