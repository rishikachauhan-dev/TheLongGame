asteriods=[3,5,-6,2,-1,4]
# Output: [-6,2,4]

# TRICK- understanding the ques we are always checking what the prev element is--LIFO-- stack ques

'''
stack=[]
result=[]
i in nums
stack.append()
check if abs(i)> abs stack -1 and sign:
stack.pop()

sign compare??
def sign()
return (nums[i]<0) ^(stack[-1]<0)
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        n=len(asteroids)
        for i in range(n):
            if asteroids[i]>0: # first all pos in stack
                stack.append(asteroids[i])
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]): #opp direction
                    stack.pop()
                if len(stack)!=0 and stack[-1]==abs(asteroids[i]): #same size
                    stack.pop()
                elif not stack or stack[-1]<0 : #same direction
                    stack.append(asteroids[i])
        return stack

# can use len(stack) or not stack

#o(n)
#o(n)