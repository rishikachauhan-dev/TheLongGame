'''
basically create 2 function of the floor and ceil and just call it in the third one
'''

'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
    
        pre=self.pre(root,key)
        succ=self.succ(root, key)
        return pre, succ
        
    def pre(self,node,key):
        pre=None #solves they none case
        temp=node
        while temp:
            if temp.data<key: #always a smaller no. not equal
                pre=temp #this scoul be the one
                temp=temp.right 
            
            else:
                temp=temp.left
            
        return pre
        
    def succ(self,node,key):
        succ=None
        temp=node
        while temp:
            if temp.data>key:
                succ=temp
                temp=temp.left
             
            else:
                temp=temp.right
            
        return succ