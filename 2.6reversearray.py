#swap numbers 2 and 4

arr= [1, 2, 3, 4, 5, 6, 7] 
l = 2 
r = 4
i=arr.index(l) 
j=arr.index(r)
arr[i],arr[j]=arr[j],arr[i]
print(arr)

#reverse an array:
num=input()
num=num[::-1]
print(num)

class Solution:
    def reverseSubArray(self, arr, l, r):
        # convert 1-based to 0-based
        l -= 1
        r -= 1
        # slicing + reverse
        arr = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]
        return arr

# # Test
# print(Solution().reverseSubArray([1, 6, 7, 4], 1, 4))

# Key difference
# arr[l:r+1][::-1] → creates a reversed copy
# arr[l:r+1] = ... → replaces in place (modifies original arr)
# arr = [1,2,3,4,5,6,7]
# l = 2, r = 4
# → l = 1, r = 3
# → arr[:1] = [1]
# → arr[1:4] = [2,3,4][::-1] = [4,3,2]
# → arr[4:] = [5,6,7]
# = [1,4,3,2,5,6,7]

