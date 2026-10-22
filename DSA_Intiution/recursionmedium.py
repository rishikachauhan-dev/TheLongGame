#ALWAYS do a stack and recusion flow--dry run of the whole code

# Generate all binary strings--------------------------------------
'''
2 - consecutive and non-consecutive
1:consecutiv
choice1: subset[index]="0" call recusrsion(index+1,subset,nums,result)
choice 2 subset[index]="1", call recusrsion(index+1,subset,nums,result)
result.append(""join(subset))
start with subset=["0"]*n

   [0,0] both zero
   /   \
[0,1] -> [0,1]
        \
        [1,1]

first choice 0, call till 0
backtrack-overwrite last call
second choice [0,1]
backtrack second last call [1,]


2: non-consecutive
flag after choice 0 flag=False, after 1 flag= True

choice 1: 0, flag false
choice 2 if flag==False
        subset[index]=1, call recusion index+1, True, nums,result---to store the value in result
        clean the slate- subset[index]=0

INSTEAD
'''
def solve(self, index, arr, result):

        # Base case
        if index == len(arr):
            result.append("".join(arr))
            return

        # Choice 1: Always place '0'
        arr[index] = '0'
        self.solve(index + 1, arr, result)

        # Choice 2: Place '1' only if previous is not '1'
        if index == 0 or arr[index - 1] != '1':
            arr[index] = '1'
            self.solve(index + 1, arr, result)

    def generateBinaryStrings(self, n):
        arr = [''] * n
        result = []

        self.solve(0, arr, result)
        return result

# Generate Paranthesis----------------------------------------------------

'''
always start with (
total=0, +1:(, -1: )

edge cases
if total<0- more closing brackets, return and add  subset[index]"(" call recursion total+1--choice 1
choice 2--add subset[index]")"

base case---when to stop?
1. when index>=len(subset), ---index+1 in recusive calls to stop that
2. when total > len(subset)//2 --means more open brackets
3.if total<0- more closing brackets,-- here it stops ) at 0 index cuz it makes -1 first
'''
# Learn All Patterns of Subsequences

# Combination Sum
'''
pick:call nums index till its <= target call(index, target, total+nums[index])

not pick- index+1

sort first so if larger no. no point in the code to keep running.--sorting for pruning

stop?
total==target
total>target or index>=len(subset)
'''
# Combination Sum-II
'''
no duplicate subsets
#Brute- sort add to set if in set skip, return set

#Optimal-
pick not pick like subsequnce with sum

for handling duplicates-
sort nums then a loop for i in range(index to n)- check if i> index (avoid pickin the same element for the same index) and nums[i]!==nums[i-1] then continue to append
'''

# Subset Sum-I
'''
1 choice- each index add by index+1 into the sum: sum+arr[index]
2 choice-each index add the no. itself as the sum
'''


# Combination Sum - III
'''
subset=k, and sum=n

1 choice loop i from 1 to 10 exclusive,
then select subset add i and sum+1 till its not >n
return, pop(), next i+1, option in same recursion
'''
# Letter Combinations of a Phone number
'''
dic char{
key : "abc", till 9}

for i in char[digit[ind]]:
subset.append(i) till subset len>=digits
index+1, if till digits add to result, return to i=1
pop is value next i igteration

'''