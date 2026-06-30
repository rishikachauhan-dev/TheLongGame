'''
        [ 1 ]          <-- Root Node
       /     \
    [ 2 ]   [ 3 ]      <-- Parent / Child Nodes
   /     \
[ 4 ]   [ 5 ]          <-- Leaf Nodes (No children)

'''
class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)

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
def preorder(node):
    #base case
    if node==None:
        return
    print(node.val, end=' ')
    #call 1
    preorder(node.left) #till all left done then right
    preorder(node.right)

preorder(one)