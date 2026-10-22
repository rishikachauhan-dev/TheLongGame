'''
Parameters = current node + current depth
Base Case
Process current node
Explore left choice
Explore right choice'''

# O(n) time and O(h) recursion space where h is the tree height
class Solution:
    def dfs(self,node,jump):
        #base case:
        if not node:
            return

        #update ans
        self.maxi=max(self.maxi,jump)
        self.dfs(node.left,jump+1)
        # jump=1 #reset jump is saved local to that call
        self.dfs(node.right,jump+1)
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # return maxi
        self.maxi=0
        self.dfs(root,1)
        return self.maxi
    
#Efficent way to write-----------Recursive
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root==None:
        return 0
    left=self.maxDepth(root.left)
    right=self.maxDepth(root.right)

    return 1+max(left,right) # witht his return 1 its calculation jumps for last leaf node 1+0+0=1, then 1+1=2 (by backtrack)
#--------------------------------------------------
# Iterative Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        height=0
        queue=deque([root])
        while queue:
            level=[]
            height+=1 # update after tracking level
            for _ in range(len(queue)):
                e=queue.popleft()
                level.append(e)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return height
#Tc-o(n), o(h)