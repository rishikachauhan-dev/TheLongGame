class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val) #this way return the node
        temp=root
        while True: # basic loop going
            if val<temp.val: # val is less then the root means go more left to add it to left
                if temp.left is None: # check then go left
                    temp.left=TreeNode(val)
                    break # always BREAK!! no need to go further only one value
                temp=temp.left# keep going on

            else:
                if temp.right is None:
                    temp.right=TreeNode(val)
                    break
                temp=temp.right
        return root