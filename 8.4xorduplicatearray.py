# Python code to find the 
# repeated elements in the 
# array where every other
# is present once

# Function to find duplicate
def findDuplicate(arr):

    # Find the intersection 
    # point of the slow and fast.
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Find the "entrance"
    # to the cycle.
    ptr1 = arr[0]
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]
        
    return ptr1
    
#---by BIT
def find_duplicate(arr):
    answer = 0
    n = len(arr)

    # XOR all the elements with 0
    for i in range(n):
        answer = answer ^ arr[i]

    # XOR all the elements with no from 1 to n
    # i.e   answer^0 = answer
    for i in range(1, n):
        answer = answer ^ i

    return answer
#  This only works if:

# 1. Are numbers from 1 to n-1?
# 2. Exactly one duplicate?

'''for gen case: '''
def find_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return x
        seen.add(x)
