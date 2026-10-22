'''Balanced tree condition is:
 abs(height(left subtree) - height(right subtree)) <= 1'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # should be equal from left and right
        # recursion
        def height(node):
            #base case
            if not node:
                return 0

            #operation
            left=height(node.left) # no self in helper function
            if left==-1:
                return -1
            right=height(node.right)
            if right==-1:
                return -1
            # return z=abs(lefty-righty) cant assign like this to return

            #now difference
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)

        z=height(root)
        
        if z==-1:
            return False
        return True 
'''line 33-37'''

        #     return 1+max(left,right) # the main increment
        # return balanced(root)!=-1

'''
Call height(3):
node=3, not None → go to operation.
left = height(9)
height(9): left = height(None) = 0, right = height(None) = 0
abs(0-0) = 0 ≤ 1 → return 1 + max(0,0) = 1 ✅
So left = 1
left != -1 → continue. right = height(20)
height(20): left = height(15)
height(15): both children None → abs(0-0)=0 → return 1
right = height(7) → returns 1
abs(1-1) = 0 ≤ 1 → return 1 + max(1,1) = 2 ✅
So right = 2
abs(1-2) = 1 ≤ 1 → return 1 + max(1,2) = 3
z = 3, which is not -1 → return True ✅ Balanced!
'''