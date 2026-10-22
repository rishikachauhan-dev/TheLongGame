#search in bst
class Solution:
    def  doesRepresentBST(self, arr):
        # code here
        for i in range(len(arr)-1): #i is the vaule here !! -1 for the index error
            if arr[i]>arr[i+1]:
                return False
        return True
    
#nodes at i level
class Solution:
    def countNodes(self, i):
        # Code here
        if i<1:
            return None
        return  1<<(i-1)

#search in bst
'''
temp=root
        result=[]
        while temp:
            if temp.val==val:
                result.append(temp.val)
                result.append(temp.left.val)
                result.append(temp.right.val)
            elif val<temp.val:#
                temp=temp.left
            else:
                temp=temp.right 
        return result 

BST Debugging Mistakes

1. Forgot to move pointer
❌ temp.right
✅ temp = temp.right

2. Accessing child without checking
❌ temp.left.val
❌ temp.right.val
✅ if temp.left:
       result.append(temp.left.val)
   if temp.right:
       result.append(temp.right.val)

3. Didn't stop after finding node
❌ while loop continues
✅ return result
(or break)

4. Infinite loop symptom
If temp is never updated (left/right), while temp: runs forever.

Memory Rule:
Always ask in tree traversal:
• Did I move my pointer?
• Can this child be None?
• Do I need to stop after finding the answer?
'''
'''temp = root
result = []

while temp:

    if temp.val == val:

        result.append(temp.val)

        if temp.left:
            result.append(temp.left.val)

        if temp.right:
            result.append(temp.right.val)

        return result

    elif val < temp.val:
        temp = temp.left

    else:
        temp = temp.right

return result
The ques wants to return the ans in root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # RETURN ROOT not result as a list
        temp = root

        while temp:

            if temp.val == val:
                return temp # node automatically has the subtree with it 

            elif val < temp.val:
                temp = temp.left

            else:
                temp = temp.right  
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        while root:
            if root.val==val:
                return root
            elif root.val > val:
                root=root.left # if greater means need smaller
                temp=root
            else:
                root=root.right
                temp=root
        return temp

        