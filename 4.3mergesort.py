nums=[5,1,3,5,4,9,8,2,6]
def merge_array(left, right):
    temp=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    if i<n:# exhaust if i left # duplicates
        while i<n: # continue if less
            temp.append(left[i])
            i+=1
    if j<m:
        while j<m:
            temp.append(right[j])
            j+=1
    return temp

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2#4
    left_arr=arr[:mid]#[5,1,3]
    right_arr=arr[mid:]#[5,4,9,8,2,6]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)

print(merge_sort(nums))
print(merge_sort(arr=nums))
print(nums)



# Example: Merge sort on [5,3,1,2]
# Step 1 – Split
# [5,3,1,2]  
#  → [5,3]  and  [1,2]
# (recursive calls keep splitting until single elements)

# Step 2 – Merge
# Now we need to merge [5,3].
# Left = [5], Right = [3]
# To combine, we can’t directly overwrite the array because we’d lose numbers.

# So computer makes a temporary array:
# temp = []
# compare 5 and 3 → pick 3 → temp = [3]
# append 5 → temp = [3,5]
# Return temp.

# Step 3 – Merge [1,2]
# Same idea → temp = [1,2].

# Step 4 – Merge [3,5] and [1,2]
# New temporary array of size 4 is created.

# temp = []
# compare 3 and 1 → temp=[1]
# compare 3 and 2 → temp=[1,2]
# append rest → temp=[1,2,3,5]

# ❓ Now your doubt

# You saw just one list like temp=[] in the code.
# But computer actually creates a new result for every merge step.
# So as N items are merged at the top level, that temporary result can be as large as N.

# Maximum extra memory needed at once ≈ N (for the biggest merge).
# Recursion stack adds another log N.
# So overall = O(N), not O(1).
# 💡 Key idea
# Constant space (O(1)) = no matter how big input is, extra memory never grows (e.g., swap in place).
# Merge sort needs a buffer proportional to array size for merging → O(N).


#optimal cuz previous was creating extra arrays
def merge(arr, l, m, r):
    temp = []
    i, j = l, m+1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    arr[l:r+1] = temp   # copy back

def merge_sort1(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort1(arr, l, m) # m inclusive funct is inclusive
        merge_sort1(arr, m+1, r)
        merge(arr, l, m, r)
# list slicing is exclusive

#better code for interview forget gfg code 

#but for clarity no k doest not chnage the original array it overwrites after it gas dine thar=t part of dividing