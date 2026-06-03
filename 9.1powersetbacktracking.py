class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def func (ind,subset):
            if ind>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[ind])
            #pick
            func(ind+1,subset)
            subset.pop()
            func(ind+1,subset)
        func(0, [])
        return result
'''
| Part | Meaning                 |
| ---- | ----------------------- |
| `0`  | start from index 0      |
| `[]` | current subset is empty |


You → func(0, [])
       ↓
    recursion tree runs
       ↓
    fills result

But defining ≠ running ❌

So you must call it once to start the process else it will be null/empty

Outer function = setup
Inner function = logic
func(0, []) = execution trigger
'''

#TC-o(2^n)
#SC=o(n) stack memeory fills till n then pops fills again