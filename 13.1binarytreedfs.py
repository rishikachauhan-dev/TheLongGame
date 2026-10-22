'''
        [ 1 ]          <-- Root Node
       /     \
    [ 2 ]   [ 3 ]      <-- Parent / Child Nodes
   /     \
[ 4 ]   [ 5 ]          <-- Leaf Nodes (No children)

'''
class Root:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

one=Root(1)
two=Root(2)
three=Root(3)
four=Root(4)
five=Root(5)

one.left=two
one.right=three
two.left=four
two.right=five

print(one) #memory location
print(one.val) 
print(one.left) #should have same address as two
print(two)#should have same address with one.left
# print(one.right.left.left.val) #None.val?--attribute error

#--------------------
#DFS: Preorder Traversal- (Root-Left-Right)
def preorder(root):
    #base case
    if root==None:
        return
    print(root.val, end=' ')
    #call 1
    preorder(root.left) #till all left done then right
    preorder(root.right)

preorder(one)

#DFS: Inorder (Left-Root-Right)---------------

def inorder(node):
    #base case
    if node==None:
        return
    inorder(node.left)
    print(node.data)
    
    inorder(node.right)
inorder(one)


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

#DFS: Postorder(Left-Right-Root)---------------

def postorder(root):
    #base case
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
    
    
postorder(one)

'''
Tree:
4
First:

postorder(4.left)

But

4.left = None

Returns immediately.
Then

postorder(4.right)

Also None.
Now both children are done.

Finally:
print(4)'''


'''Conclusion: head and Tail recusrsion ka khel'''