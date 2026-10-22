#Delete a node

root = [5,3,6,2,4,null,7]
key = 3

'''create function that handles delete,
create basic bst template and call it'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            return self.deletion(root)
        temp=root
        while temp:
            if temp.val>key:
                if temp.left is not None and temp.left.val==key:
                    temp.left=self.deletion(temp.left)# the subtree gets attached here
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is not None and temp.right.val==key:
                    temp.right=self.deletion(temp.right)# the subtree gets attached here
                    break
                else:
                    temp=temp.right

        return root
    def deletion(self,node):
        if node.left is None:
            return node.right # after returing temp.left will have this as a subtree

        elif node.right is None:
            return node.left

        else:
            rightChild=node.right
            lastRight=self.findLastRight(node.left) # will get attacged to the temp.left's right end
            lastRight.right=rightChild
            return node.left # the now left subtree which has the 8 subtree attached and also the subtree is still attached with 6

    def findLastRight(self,node):
        while node.right is not None:
            node=node.right
        return node

#o(n+logn+logn) ??

# the vice versa:------------------------
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int)-> Optional[TreeNode]:
        if root is None:
            return None
        temp=root
        if root.val==key:
            return self.deletion(root)
        while temp:
            if temp.val>key:
                if temp.left is not None and temp.left.val==key:
                    temp.left=self.deletion(temp.left)
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is not None and temp.right.val==key:
                    temp.right=self.deletion(temp.right)
                    break
                else:
                    temp=temp.right
        return root

    def deletion(self,node): # this will return the node to be joined to the roots left, here the right subtree attached to the del node
        if node.left is None:
            return node.right # we are returning what we what to attach to the del's right's smallest
        elif node.right is None:
            return node.left

        else:# when it the del has a whole subtree
            #find the right's ka left side
            '''richild=node.right''' 
            lechild=node.left #2=3.left # lc is the 2 subtree
            lastlechild=self.findlastlechild(node.right) #(4) 
            # attach that and return
            lastlechild.left=lechild #4.left=2 # debugged created double loop
            return node.right # the node with the attached tree

    def findlastlechild(self,node):
        while node.left is not None:
            node=node.left
        return node
# better debug, but couldnt guess the probleem of doubleloop
#TC-o(logN), or o(N), sc o(1)


#--------------------------efficient code
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root != None:
            if key > root.val:
                root.right = self.deleteNode(root.right, key) 
            elif key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key == root.val:
                if not root.left and not root.right: # 第一种
                    return None
                elif not root.left and root.right: # 第二种
                    return root.right
                elif not root.right and root.left: # 第二种
                    return root.left
                else: # 第三种，我们取左子树的最大值
                    # 找到左子树的最大值，赋值给左子树的root，然后再用deleteNode那个node删掉
                    curr_node = root.left
                    while curr_node.right:
                        curr_node = curr_node.right
                    root.val = curr_node.val
                    root.left = self.deleteNode(root.left, curr_node.val)

        return root 