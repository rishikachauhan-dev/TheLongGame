nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]  # Example array
k = 3  

result=[]
def find1(index, subset,total): # recur func
    #base case 1
    if index>=len(nums):
        return
    #base case 2
    if total==k:
        result.append(subset.copy())

    if total>k:
        return

    #operation

    #1.add
    subset.append(nums[index]) #pick
    #2. update
    sum=total+nums[index]

    #inclusion
    find1(index+1,subset,sum)

    #backtrack
    subset.pop()
    # total+=0 # reset?
    sum=total

    #exclusion
    find1(index+1,subset,sum) #not pick


find1(0,[],0)
print(result)

#Cleaner version-------------
result = []

def find(index, subset, total):
    # base case
    if index == len(nums):
        if total == k:
            result.append(subset.copy())
        return

    if total > k:
        return

    # operation
    subset.append(nums[index])

    #pick
    find(index + 1, subset, total + nums[index])
    ''' total += nums[index]
    find(index + 1, subset, total)''' #if this line used then we have to undo the total

    # backtrack
    subset.pop()
    '''total-=nums[index]''' #with each pop it subtracts that value at the index thats whats happening above----no need for this cuz
    # not picking meeans it goes back to the previous cond. when it was not taken ans so the total was what it was before

    # not pick
    find(index + 1, subset, total)


find(0, [], 0)

''' no need for sum reset
Call stack:

[ total=0 ]
   ↓
[ total=2 ]
   ↓
[ total=5 ]

pop 5 → back to 2
pop 2 → back to 0'''