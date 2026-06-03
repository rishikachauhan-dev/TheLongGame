'''def find(index, total):
    
    if index >= len(arr):
        if total == target:
            return 1 if total==target else 0
    if total > target:
        return 0
    
    #opration
    # total+=arr[index]
    # pick+
    pick=find(index + 1, total+=arr[index])
    
    # backtrack
    # total-=arr[i]
    
    # not pick
    notpick=find(index + 1, total)
    
    return pick+notpick
return find(0, 0)'''

def find(index, total):
    # base case
    if index == len(arr):
        return 1 if total == target else 0 #pick 1 if target reached else 0
    
    if total > target:
        return 0
    
    #opration
    # total+=arr[index]
    # pick+
    pick=find(index + 1, total+arr[index])
    
    # backtrack
    # total-=arr[i]
    
    # not pick
    notpick=find(index + 1, total)
    
    return pick+notpick
    
return find(0, 0)


#TC-2^n Sc-o(n) storing those retunr 1 and 0 in memory

#TLE use DP
