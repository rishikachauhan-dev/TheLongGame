#Is set?----------------
if (num & (1<<(i)))!=0: # brackets imp cuz fist and then comapre with 0
        return True
    else:
        return False


#Even odd---------------
if n & 1:
    # print("Odd")
    return False

else:
    # print("Even")
    return True

#Power of 2--edge case n=0 is false cuz no power of 2 gives 0

# if (n&(n-1))!=0:
    #     return False
    # else:
    #     return True
    return n > 0 and (n & (n - 1)) == 0

#Count bits-----------------
count = 0
        
while n > 0:
    count += (n & 1)   # check last bit
    n >>= 1            # shift right

return count

# tc=logn
# other trick is by turning off (&) every bit in the no. by n&n-1 count turn offs
count=0
while n!=0:
    n=n&(n-1)
    count+=1
return count

#tc-no. of set bits
