class Solution:
    def solve(self,node,limit): # recursion
        if node is None:
            return True
        
        # base case
        if not limit[0]<node.val<limit[1]:
            return False
        
        left=self.solve(node.left,[limit[0],node.val]) # will return T/F
        if left==False: # in the recursove loop to sent that to the parent call
            return False
        
        right=self.solve(node.right,[node.val,limit[1]])
        return left and right # t&f=f

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root,[float('-inf'),float('inf')]) #-inf not infi and - inside quotation