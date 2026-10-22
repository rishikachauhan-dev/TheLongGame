class Solution:
    def solve(self,node,p,q):
        if node is None:
            return None
        # the loop
        if node==p or node==q:
            return node

        left=self.solve(node.left,p,q)
        right=self.solve(node.right,p,q)

        if node.left is None and node.right is None:
            return None

        elif left is None: # debugged not node but the left value to pass
            return right

        elif right is None:
            return left
        return node #LCA

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)


    #------------------------------------better
    def lowestCommonAncestor(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root  # Current node is LCA
    return left if left else right

'''
1. Start at root 1
Recurse left to 2, recurse right to 3
2. At node 2:
Recurse left to 4 → matches p=4 → return 4
Recurse right to 5
Recurse left to 6 → not 4 or 7 → return None
Recurse right to 7 → matches q=7 → return 7
At 5: left=None, right=7 → return 7
At 2: left=4, right=7 → both found! → return 2
✅ So node 2 is the LCA of 4 and 7.

3. At node 3:
Neither 4 nor 7 is in this subtree → returns None
4. Back at root 1:
left=2, right=None → return 2
'''