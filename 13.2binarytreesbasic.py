# Introduction to Trees
print(2 ** (i - 1))
print(1<<(i - 1))
'''
In a maximum/full binary tree, every node has 2 children, so the number of nodes doubles at each level.

Level	Maximum Nodes
1	1
2	2
3	4
4	8
5	16

Notice:

Level 1 -> 2^0 = 1
Level 2 -> 2^1 = 2
Level 3 -> 2^2 = 4
Level 4 -> 2^3 = 8
Level 5 -> 2^4 = 16

Therefore:

Maximum nodes at level i = 2^(i-1)
'''

# Create Binary Tree
nodes = [1, 2, 3, 4, 5, 6, 7]
'''This is a mapping question, not a traversal question.

For a complete binary tree stored in level order, the indices follow a fixed pattern:

If a node is at index i:

Left Child  = 2*i + 1
Right Child = 2*i + 2'''

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, nodes):
        # code here
        if not nodes:
            return None
            
        treeNode=[]
        for i in nodes: #o(n)
            treeNode.append(Node(i)) # individual nodes class node
            
        for i in range(len(nodes)): #o(n)
            left=(2*i)+1 # this can go out of index for the last ind
            right=(2*i)+2
            
            '''left = 2*0+1 = 1
            right = 2*0+2 = 2
            
            Meaning:
            
            Node at index 1 becomes left child
            Node at index 2 becomes right child
            
            Execute:
            
            tree_nodes[0].left = tree_nodes[1]
            tree_nodes[0].right = tree_nodes[2]'''
            
            if left<len(nodes): # <=? cuz 0 to len(nodes)-1 #o(1)
                treeNode[i].left=treeNode[left] # if left crosses len then its  None and becomes a leaf node, treende at 0.left=treenode at left index
            
            if right<len(nodes): #o(1)
                treeNode[i].right=treeNode[right]
                
        return treeNode[0]
            
        
# Binary Tree Traversals in Binary Tree---------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #root-left-right
        if root is None:
            return []
        return([root.val]+
        self.preorderTraversal(root.left)+
        self.preorderTraversal(root.right))# ans in a list
    #Better approach

class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)   # Root
            dfs(node.left)            # Left
            dfs(node.right)           # Right

        dfs(root) # link to node
        return result
    
'''
dfs(1)
append 1

    dfs(2)
    append 2

        dfs(4)
        append 4
        left=None
        right=None
        return

        dfs(5)
        append 5
        left=None
        right=None
        return

    return

    dfs(3)
    append 3
    left=None
    right=None
    return
'''