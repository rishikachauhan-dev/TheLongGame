'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans=[]
        result={}
        queue=deque([(root,0)])
        while queue:
            e,line=queue.popleft()
            # if line>=0:
            result[line]=e.val
            if e.right:
                queue.append((e.right,line+1))
        for values in sorted(result.items()):
            ans.append(values[1])
        return ans
 did not pass the test case
'''
#Brute----------------
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            size=len(queue)# afte appending all we will couny
            for i in range(len(queue)):   
                e=queue.popleft()
            # if line>=0:
                # if i==len(queue)-1: wrong instead use size var cuz it will store curr len after popleft the size will dec
                if i==size-1:
                    result.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return result
#tc=o(n), o(n+n)

#Optimal--------------
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def reversePost(node,level,result):#left-right-root, here root-right-left
        
            if not node:
                return []
            if level==len(result):# this is the way to find the rightmost
            #i.e=at each level if the result is equal means it has already called the right recursive call
                result.append(node.val)
            if node.right:
                reversePost(node.right,level+1,result)
            if node.left:
                reversePost(node.left,level+1,result)

        result=[]
        reversePost(root,0,result)
        return result