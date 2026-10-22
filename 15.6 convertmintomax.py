arr=[4,6,9,12,16,13,19,21]
n=len(arr)
'''
for i in range(n//2-1,-1,-1):
        si=i
        lech=2*i+1
        rech=2*i+2
        if lech<n and arr[lech]>arr[si]:
            #swap
            # arr[lech],arr[si]=arr[si],arr[lech]
            si=lech
        if rech<n and arr[rech]>arr[si]:
            #swap
            # arr[rech],arr[si]=arr[si],arr[rech]
            si=rech # compare right with left child
        if si==i: #swap here with the largest child : herre moving the smallest element DOWN
            break
        arr[i],arr[si]=arr[si],arr[i]
        # si=i this is wrong -- start with a new index
        i=si
print(arr) '''
# For every parent:
# 1. Find left child
# 2. Find right child
# 3. Find the LARGEST of the 3
# 4. If parent isn't largest → swap
# 5. Continue from the new position

'''
for chooses which parent to process.
while handles how far that parent needs to move downward.'''

for i in range(n//2-1,-1,-1):
    
    while True: 
        si=i # RESET for this level inside cuz, You need to start the next iteration by saying:"Currently, assume the parent is the largest."
        lech=2*i+1
        rech=2*i+2
        if lech<n and arr[lech]>arr[si]:
            #swap
            # arr[lech],arr[si]=arr[si],arr[lech]
            si=lech
        if rech<n and arr[rech]>arr[si]:
            #swap
            # arr[rech],arr[si]=arr[si],arr[rech]
            si=rech # compare right with left child
        if si==i: #swap here with the largest child : herre moving the smallest element DOWN
            break
        arr[i],arr[si]=arr[si],arr[i]
        # si=i this is wrong -- start with a new index
        i=si #current index as smallest, continue from new position, then above assume the pos is smallest
print(arr)
'''
FOR LOOP
   ↓
Which parent should I heapify?
   ↓
3 → 2 → 1 → 0


WHILE LOOP
   ↓
How far does THIS parent need to move down?
   ↓
0 → 2 → 6 → ...
'''