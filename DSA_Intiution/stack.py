# Next Greater Element
'''
Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
'''

'''result
stack
while i < len(arr)
    if i> previous element of stack
    add to result
    if not i+=1

add i to stack'''
'''
NO:
result=[-1]*n by default
stack
reverse loop: 
for i in range(n-1):
    if stack not zero and stack[-1]<i: #2<3-False, should be greater
        stack.pop() # remove it
    ans[i]=stack[-1]#add the stack top element to the result till its empty
    when stack is empty means the last element doesnt have anything greater so ans[i]=-1 already! by default  
    add i to stack

'''

# Next Greater Element 2
'''
Circular way

'''
# Asteroid Collision