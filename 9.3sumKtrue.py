arr = [1, 2, 3, 4, 3]  # Example array
k = 3  

def find(index, total):
    # base case
    if index >= len(arr):
        return total == k 
    
    if total > k:
        return False
    
    #opration
    total+=arr[index]

    # pick
    if find(index + 1, total):
        return True
    
    #backtrack 
    total-=arr[index]
    
    # not pick
    if find(index + 1, total):
        return True
    
    return False # this is the line if return !=K

print(find(0, 0))