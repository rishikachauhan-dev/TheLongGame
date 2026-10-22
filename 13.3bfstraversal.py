# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

root = [3,9,20,null,null,15,7]

'''
def bfs(node):
    result=[]
    queue=deque([])
    if not node:
        return
    queue.append(node) # even one node everything will connect its linked
    while len(queue)!=0:
        e=queue.popleft() #popleft for deque o(1)
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result
So, not wright way to code logic good         
            '''

#but Leetcode outputs by levels
'''
Let's use this tree:

        3
       / \
      9   20
         /  \
       15    7

Expected answer:

[[3], [9,20], [15,7]]
'''
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[] #final result
        queue=deque([root])#3
        while queue:
            level=[]
            for _ in range(len(queue)): #1|2:queue=9,20
                e=queue.popleft()#e=3|9
                level.append(e.val)  #[3]|[9,20]
                if e.left: #9| None
                    queue.append(e.left) #9 added
                if e.right:
                    queue.append(e.right) # 20 added
            result.append(level)#[[3],[9,20]]
        return result

 