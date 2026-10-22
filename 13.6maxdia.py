class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        # dia=0
        def solve(node):
            # nonlocal dia
            if not node:
                return 0
            left=solve(node.left)
            right=solve(node.right)
            self.dia=max(self.dia,left+right) #0+0 on first call
            # dia=max(dia,left+right)
            return 1+max(left,right)
        solve(root)
        return self.dia
        # return dia
'''The commented works this way to avoid attribute error '''
#o(n), o(n)