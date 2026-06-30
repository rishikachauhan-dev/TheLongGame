# Generate all binary strings
'''
2 - consecutive and non-consecutive
1:consecutiv
choice1: subset[index]="0" call recusrsion(index+1,subset,nums,result)
choice 2 subset[index]="1", call recusrsion(index+1,subset,nums,result)
result.append(""join(subset))
start with subset=["0"]*n

2: non-consecutive
flag after choice 0 flag=False, after 1 flag= True

choice 1: 0, flag false
choice 2 if flag==False
        subset[index]=1, call recusion index+1, True, nums,result---to store the value in result
        clean the slate- subset[index]=0


'''
# Generate Paranthesis

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


# Combination Sum - III
# Letter Combinations of a Phone number