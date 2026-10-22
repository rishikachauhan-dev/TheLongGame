#min val in bst

'''
class Solution:
    def minValue(self, root):
        if root is None:
            return -1
        temp=root
        while root.left:
            root=root.left
            temp=root
            
        return temp
'''
#Min will always be at the leftest node
class Solution:
    def minValue(self, root):
        if root is None:
            return -1
        while root and root.left:
            root=root.left
        return root.data
#-------------------------------------
#CEIL
'''
class Solution:
    def findCeil(self, root, x):

        ceil = -1

        while root:

            if root.data == x:
                return root.data

            elif root.data > x:
                ceil = root.data
                root = root.left

            else:
                root = root.right

        return ceil

4. Wrong direction
node > x  → go LEFT
node < x  → go RIGHT

Memory Rule:
Greater? Save it and go left.
Smaller? Ignore it and go right.
Equal? Return immediately.
'''
class Solution:
    def findCeil(self, root, x):

        ceil = -1

        while root:

            if root.data == x:
                return root.data

            elif root.data > x: # first root> x # this loop will checl ig we have min element grater that x15.1
                ceil = root.data
                root = root.left # try left

            else:
                root = root.right

        return ceil
#or this works too
class Solution:
    def findCeil(self,root, x):
        # code here
        ceil=-1
        while root:
            if root.data>=x:
                ceil=root.data
                root=root.left
                
            else:
                root=root.right
        
        return ceil
#----------------------------------
#FLOOR
class Solution:
    def findMaxFork(self, root, k):
        #code here
        floor=-1
        while root:
            if root.data<=k:
                floor=root.data
                root=root.right
            else:
                root=root.left
        return floor