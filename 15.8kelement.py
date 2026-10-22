class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        n=len(heap)
        for i in range(len(nums)): #min heaps:--keep the smalles element at top that will be the kth element, shift down if larger, also if n>k then remove element from top and swap??
            heap.append(nums[i]) # gonna be at last so shift up
            self.up(i)
    
            if n>k:
                heap.pop(0)

        def up(self,i):
            while nums:
                p=i-1//2
                if nums[p]>nums[i]:
                    nums[p],nums[i]=nums[i],nums[p]
                    self.up(p)   
        return heap[0]
#close?? TLE


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap to keep track of the k largest elements
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # If heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap) # here only the smallest value comes out?
        
        # The root of the min-heap is the k-th largest element
        return min_heap[0]

# Example usage:
# solution = Solution()
# print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)) # Output: 5


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i, val in enumerate(nums):
            heap.append(val)
            
            # Shift Up: Maintain Min-Heap property
            # Start from the current index (len(heap) - 1) and move up
            curr = len(heap) - 1
            while curr > 0:
                p = (curr - 1) // 2  # Correct parent index calculation
                if heap[p] > heap[curr]:
                    heap[p], heap[curr] = heap[curr], heap[p]
                    curr = p
                else:
                    break
            
            # If size exceeds k, remove the smallest (root)
            if len(heap) > k:
                # Swap root with last element and pop
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()
                
                # Optional: Shift Down the new root to maintain heap property
                # (Strictly speaking, for this logic, we only need the root to be valid)
                # But for a robust heap, we should re-heapify the root.
                # For this specific "k-th largest" logic, we can skip full sift-down 
                # if we only ever pop the root, but let's add it for correctness.
                if heap:
                    self._sift_down(heap, 0, k)
        
        return heap[0]

    def _sift_down(self, heap, idx, k):
        # Helper to maintain heap property after popping
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        while left < k: # Only check within the valid heap size
            if right < k and heap[right] < heap[left] and heap[right] < heap[smallest]:
                smallest = right
            elif left < k and heap[left] < heap[smallest]:
                smallest = left
            else:
                break
            
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
            left = 2 * idx + 1
            right = 2 * idx + 2

# can do it this way but heapque better TC-o(n)

#use quick sort


#------------------------------------------------------------------
import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Use a list to simulate a max-heap
        # We store negative values because heapq is a min-heap
        max_heap = []
        
        for num in arr:
            # Push negative value to simulate max-heap behavior
            heapq.heappush(max_heap, -num)
            
            # If size exceeds k, remove the "largest" element (which is the most negative)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The root is the largest of the k smallest elements (stored as negative)
        # Return the positive version
        return -max_heap[0]


import heapq
class Solution:
    def kthSmallest(self, arr, k):
        max=[]
        for i in arr:
            heapq.heappush(max,-i)
            
            if len(max)>k:
                heapq.heappop(max)
        return max[0]*-1