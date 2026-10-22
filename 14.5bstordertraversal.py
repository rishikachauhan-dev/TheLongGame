#Morris traversal for both bt and bst

'''
brute is basic recursion call, sc-o(n)
better is sc(1), ny threading
'''
#RECURSION-----------
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

#Morris Algorithm----- INORDER
result=[]
current=root
while current:
    if current.left is None:
        result.append(current.val)
        current=current.right #update it debugged # back to original, we are only appending current so we need to traverse current to each node
        
    else:
        pre=current.left

        while (pre.right is not None and pre.right!=current):#the thread
            pre=pre.right

        if pre.right is None: #connect thread # indentaton for this block
            pre.right=current
            current=current.left #current moves to left
        else:
            pre.right=None # remove thread
            result.append(current.val)
            current=current.right # next
return result

'''
 if current.left is not None:
        pre=current.left
else:
    result.append(current.val)
    current=current.right #update it debugged

this doesnt work cuz it it doesnt go to the else statement there

'''
result=[]
while root is not none:
    curr=root
    if curr.left is not none:
        pre=curr.left
        #thread?
        #print pre then the thread next into the result.
        curr=curr.left