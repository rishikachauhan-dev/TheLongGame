#quick sort--low=pivot

nums=[4,1,7,6,3,2,8]
def partition(nums,low,high):
    pivot=nums[low] 
    i,j=low,high
    while i<j:
        while nums[i]<=pivot and i<=high-1:#high=len(nums)#i=0[4] 1st loop wroks till it exceeds the cond. loop stops 7
            i+=1 #i=1, i=2[7] 
            # print(i)
        while nums[j]>=pivot and j>low:# cuz or j>=low+1? basically same meaning-> low=pivot so it will compare it with itslef which we dont need # stop j=5
            j-=1 #j=6[8], j=5[2]
            # print(j)
        if i<j:# 
            nums[i],nums[j]=nums[j],nums[i]#
        # when i and j overlaps?
    nums[low],nums[j]=nums[j],nums[low] # replace nums[low] w/ nums[j]
    return j # j? the new low


def sort(nums,low,high):
    if low<high:#0<6
        p_index=partition(nums,low,high)#
        sort(nums,low,p_index-1)#left half # this recursive call work first till last call  -1 and +1 cuz in middle its the pivot
        sort(nums,p_index+1,high)#right half

sort(nums,0,6)   
print(nums)

#Tc=o(nlogn) no extra space so o(1)
#            [4,1,7,3,2]  →  n
#            /       \
#      [1,3,2]       [7]  →  n/2
#      /    \
#    [1]   [3,2]          →  n/4
#            ...
# Depth ≈ log n
# At each depth, total comparisons ≈ n.
# n (work) × log n (levels) = n log n








# We have:
# nums = [3, 7, 1, 4, 2, 8]

# We call:
# sort(nums, 0, 5)
# 1️⃣ sort(nums, low, high)
# low = 0, high = 5
# Check if low < high: → 0 < 5 ✅ yes, so go in
# Call partition(nums, 0, 5)

# 2️⃣ partition(nums, low, high)
# pivot = nums[low]  # pivot = 3
# i, j = low+1, high # i=1, j=5

# 3️⃣ Partition loop while i < j:
# Goal: Move i right until it finds a number > pivot
# Move j left until it finds a number < pivot
# Swap nums[i] and nums[j] if i < j

# Step 3a: Move i
# while nums[i] <= pivot and i < high-1: 
#     i += 1
# nums[i]=7, pivot=3 → 7 > 3 ✅ stop
# So i = 1

# Step 3b: Move j
# while nums[j] >= pivot and j > low+1: 
#     j -= 1
# nums[j]=8 → 8 >= 3 ✅ j=4
# nums[j]=2 → 2 >= 3 ❌ stop
# So j = 4

# Step 3c: Swap i and j if i<j
# i=1, j=4 → 1 < 4 ✅ swap
# nums = [3, 2, 1, 4, 7, 8]  # 7 and 2 swapped

# Step 3d: Next iteration
# Move i: nums[i]=nums[1]=2 <= 3 → i=2
# Move i: nums[i]=nums[2]=1 <= 3 → i=3
# Move i: nums[i]=nums[3]=4 > 3 stop, i=3
# Move j: nums[j]=nums[3]=4 >= 3 → j=2
# i < j? 3 < 2 ❌ stop loop

# 4️⃣ Swap pivot into place
# nums[low], nums[j] = nums[j], nums[low]
# nums[0] (3) ↔ nums[2] (1)
# nums = [1, 2, 3, 4, 7, 8]
# Return j=2 → new pivot position

# 5️⃣ Recursion: Left half
# sort(nums, low, p_index-1)  # sort(nums, 0, 1)
# pivot = nums[0] = 1
# i=1, j=1 → loop stops
# swap pivot with itself → no change
# recursive calls: sort(nums, 0, -1) and sort(nums, 1, 1) → base case, stop

# 6️⃣ Recursion: Right half
# sort(nums, p_index+1, high)  # sort(nums, 3, 5)
# pivot = nums[3] = 4
# i=4, j=5
# move i → nums[4]=7 > 4 stop
# move j → nums[5]=8 > 4 → j=4 → nums[4]=7 > 4 → j=3
# i < j? 4 < 3 ❌ sto
# swap pivot with nums[j]=nums[3] → no change
# recursive calls: sort(nums, 3, 2) and sort(nums, 4, 5)

# 7️⃣ Right subarray sort(nums, 4, 5)
# pivot = nums[4] = 7
# i=5, j=5
# loop stops immediately → swap pivot with nums[5]? depends on code
# swap nums[4], nums[5] → 7 ↔ 8 →
# nums = [1, 2, 3, 4, 7, 8] ✅
# recursive calls → base case, stop

# ✅ Final Sorted Array
# [1, 2, 3, 4, 7, 8]
