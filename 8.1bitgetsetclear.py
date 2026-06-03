#BRUTE____ WRONG NOT THIS WAY CHECK 1NOTES

# # result.list() not this way
# result=list(num)

# #GET
# return result[i]

# #SET
# if result[i]==0:
#     result[i]=1
# return result


# #CLEAR
# if result[i]==0:
#     result[i]=1
# return result

#tc=o(n)

#--------------------------
#OPTIMAL____

# num, i = map(int, input().split()) --not necessary, but for CP

#BIT INEXING STARTS FROM RIGHT to LEFT 

#so here 3, 2,1,0 is indexed but here 4,3,2,1
# 1-based indexing in the problem
# literally type it this way


# Get ith bit
get_bit = (num >> (i - 1)) & 1 # shift num right by i, & 1 eg: 1101---0011 & 0001=0001

# Set ith bit
set_bit = num | (1 << (i - 1)) #num OR 1 left shifted

# Clear ith bit
clear_bit = num & ~(1 << (i - 1)) # num AND ~left shift

 # return get_bit, set_bit, clear_bit - ques expected to print

print(get_bit, set_bit, clear_bit)