# Middle of a LinkedList [TortoiseHare Method]
# Reverse a LinkedList [Iterative]
# Detect a loop in LL
# Find the starting point in LL
# Length of Loop in LL
# Segrregate odd and even nodes in LL
# Remove Nth node from the back of the LL
'''We use two pointers with a fixed distance between them. 
First, we move the fast pointer n steps ahead to create the desired gap. 
If the fast pointer becomes None, it means we need to remove the head node. 
Otherwise, we move both pointers together until the fast pointer reaches the last node. 
At this point, the slow pointer is positioned just before the node we want to remove. 
We then remove the target node by updating the slow pointer’s next reference.

o(n)
o(1)
'''
