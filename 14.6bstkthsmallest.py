class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        current=root
        while current:
            if current.left is None:
                result.append(current.val)
                current=current.right
            else:
                pre=current.left

                while pre.right is not None and pre.right!=current:
                    pre=pre.right #loop for threads

                if pre.right is None: #connect thread
                    pre.right=current
                    current=current.left
                else: # remove thread
                    pre.right=None
                    result.append(current.val)
                    current=current.right
        return result[k-1]

#----------------------------------------

'''
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        temp=[]
    # make it preorder than return
        def dfs(self,root,temp):
            
            #base case
            if node==None:
                temp.append(node)
            #pick
            self.dfs(node.left,temp)

            #notpick
            self.dfs(node.right,temp)

        return temp[k-2]
        
'''
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        temp = []

        def dfs(node):                          # ← param name must match usage
            if node is None:
                return                           # ← base case: just STOP, don't append
            dfs(node.left, )                     # ← left
            temp.append(node.val)                # ← append .val, not the node
            dfs(node.right)                      # ← right

        dfs(root)                                # ← actually CALL it
        return temp[k - 1]                       # ← k-1, not k-2 (0-indexed) 
#O(n) 