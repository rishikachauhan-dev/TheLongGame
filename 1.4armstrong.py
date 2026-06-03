#Mylogic-w
#Armstrong no.? : a number that equals the sum of its own digits each raised to the power of the total number of digits
# str=input('- ')
# count=len(str)
# arm=0
# for s in str:
#     s=int(s)
#     arm+=pow(s,count)
    
# print('Yes'if arm==int(str) else 'No' )


##Math Logic
number=int(input("- "))# 153
nums=number
count=0
arm=0
while nums>0:
    num=nums%10
    nums=nums//10
    count+=1
for n in str(number):
     n=int(n)
     arm+=pow(n,count)
print('Yes'if arm==int(number) else 'No') #TC-o(n) Sc o(1)

#Efficient
number = int(input("- "))
count = len(str(number))   # total digits
nums = number
arm = 0

while nums > 0:
    digit = nums % 10         # get last digit
    arm += pow(digit, count)  # add digit^count
    nums //= 10               # shrink number

print("Yes" if arm == number else "No")


# Cuz Armstrong GFG ques gave constraints-3 digit num no need to complicate and count

## optimized for gfg----
# dont print; return 
# print(type(print))
# type(return)=Boolean

#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        original = n
        arm = 0
        while n > 0:
            digit = n % 10
            arm += pow(digit,3)
            n = n // 10
        if arm == original:
            return True
        else:
            return False