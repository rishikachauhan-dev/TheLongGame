##Mylogic
#palindrome=aba
# str=input('- ')
# if str[:]==str[::-1]:
#     print('palindrome')
# else:
#     print('Not')

##Math logic
nums=int(input('- '))
num=nums
rev=0
while num>0:
    n=num%10#3 
    num=num//10#12
    rev=(rev*10)+n
if rev==nums:
     print('palindrome')
else:
    print('Not')
#TC-o(log n) SC-o(1)


#Leetcode Sol

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num=x #int(num)=x is C++
        rev=0
        while num>0:
            n=num%10  
            num=num//10 # removes last digit // means comment in c++
            rev=(rev*10)+n
        if rev==x:
            return True
        else:
            return False

