n=3

class Solution:

    def solve(self, index, path, result, n):
        
        # base case
        if index == n:
            result.append("".join(path)) # (path.copy())-cuz it stores the stack in memeory #o(n)
            return 
        
        # choose 0
        path[index] = "0"
        self.solve(index + 1, path, result, n)
        
        # choose 1
        path[index] = "1"
        self.solve(index + 1, path, result, n)
        
    def binstr(self, n):
        result = []
        path = ["0"] * n
        self.solve(0, path, result, n) # self start
        return result
# print(result)   
'''| index | path  | action           |
| ----- | ----- | ---------------- |
| 0     | `_ _` | start            |
| 0     | `0 _` | choose 0         |
| 1     | `0 0` | choose 0 → store |
| 1     | `0 1` | choose 1 → store |
| 0     | `1 _` | backtrack        |
| 1     | `1 0` | store            |
| 1     | `1 1` | store            |

No backtrackinh here- state restored by overwriting ✔
'''
#TC-o(2^n *n) Sc-o(n)

#---------------No consecutive 1's

'''intuituition
True-0/1 can put both
False-0 
now flagging the previous track;
after 1 is assigned it will next value track will be False, then next value track will be True'''

class Solution:

    def solve(self, index, flag, numbers, result):
        # Base case: If we've filled all positions, add to result
        if index >= len(numbers):
            result.append("".join(numbers))  # Convert array to string
            return
        
        # Choice 1: Always place '0' at current position
        numbers[index] = "0"
        self.solve(index + 1, True, numbers, result)  # Next position can have 0 or 1
        
        # Choice 2: Place '1' only if flag is True (no consecutive 1's)
        if flag == True:
            numbers[index] = "1"
            self.solve(index + 1, False, numbers, result)  # Next position can only have 0 # flag that pos to False now
            numbers[index] = "0"  # Backtrack: reset to "0" for clean slate

    def binstr(self, n):
        numbers = ["0"] * n  # Initialize array with all "0"s
        result = []          # List to store all valid binary strings
        self.solve(0, True, numbers, result)  # Start from index 0, flag=True
        return result
print(result)

#Tc(2^n) not mention copy as *n tho, sc-o(n)