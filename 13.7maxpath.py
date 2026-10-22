class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf') #infinity full is a bug
        def solve(node):
            if not node:
                return 0
            leftsum=solve(node.left) # here the return gets updated in asum
            if leftsum<0:#
                leftsum=0 #path sum
            rightsum=solve(node.right)
            if rightsum<0:
                rightsum=0
            currNode=leftsum + node.val+ rightsum
            self.maxi=max(self.maxi,currNode)
            # return one side upward
            return node.val+max(leftsum,rightsum)#path sum
        solve(root)
        return self.maxi
#o(n), o(n)
####smaller line of code

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum=float('-inf') #outside helper func else int not iterable sum is lost as soon as it finishes
        #best optimal path
        def bestpath(node):
    
            if node is None:
                return 0

            left=max(0,bestpath(node.left))

            right=max(0,bestpath(node.right))
        
            curr=node.val+left+right #here we will get the right left val as 0+curr+0
            self.sum=max(self.sum,curr)

            return node.val+max(left,right) # curr node will add max then pass
        bestpath(root)
        return self.sum