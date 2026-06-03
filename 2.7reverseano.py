#Leetcode problem
#should be within 32bit = 2^31-1 is the limit
#include negative numbers
# by default x is an integer

x=int(input())#given cond.
sign=-1 if x<0 else 1
x=abs(x)
rev=int(str(x)[::-1])
rev*=sign #multiply by sign which was removed

# now chwck bit
if rev <-2**31-1 or rev> 2**31-1:
    print (0)
print(rev)



class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1      # remember if it's negative
        x = abs(x)                     # work with positive for now
        rev = int(str(x)[::-1])        # reverse digits as string
        
        rev *= sign                    # restore the sign
        
        # Check 32-bit integer range
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev


#optimal code
class Solution(object):
    def reverse(self, x):
        rev = int(str(abs(x))[::-1])
        if rev>=2**31-1 or rev<-2**31:
            return 0
        if str(x)[0]=="-": # [0] means the first charac of str x if=='-'
            return -rev
        return rev


        