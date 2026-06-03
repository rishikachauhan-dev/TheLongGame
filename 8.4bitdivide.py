##Divide w/o sign--------------------
#Tc-o(-

def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    #this is to stop over flow so when it is pos we retur num-1 
    '''-2147483648 / -1 = 2147483648
    2147483648 > 2^31 - 1 (2147483647)---exceeds 32 bit integer
    
    | Case       | Result | Valid?     |
    | ---------- | ------ | ---------- |
    | -2^31 / 1  | -2^31  | ✅          |
    | -2^31 / -1 | +2^31  | ❌ overflow |
'''

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0

    while dividend >= divisor:
        shift = 0

        while dividend >= (divisor << (shift + 1)): #3*(2^i)  #logn
            shift += 1

        result += (1 << shift)
        dividend -= (divisor << shift)

    return result * sign

'''| Case          | Expected     |
| ---------------- | ------------ |
| 0 / anything     | 0            |
| smaller / bigger | 0            |
| same numbers     | 1            |
| negative mix     | sign handled |

The sign with XOR
True ^ True   = False
False ^ False = False
True ^ False  = True
False ^ True  = True

Same signs → positive result
Different signs → negative result
'''



'''
Pseudocode-
22/3=3 - 7 times?

divisor, dividened
dividend-divisor
'''
dividend=15
divisor=3



dividend=abs(dividend)
divisor=abs(divisor)

while dividend >= divisor: #15>3?
    i=0
    while dividend >= divisor<<(i+1): #1111>=11, 11<<1= 1111>=110? till its not i==3 it stops? cuz 3 is being shifted <<1  which multiplied by 2
        # || 3>=3?, 11<<1=110=6  it stops

        i+=1
    # so here i=2 || i=0
    ans+=(1<<i) # 100= 2^2? 4 || 2^0=1, 4+1 =5
    dividend-=(divisor<<i) # 15-(1100)=15-12=3 so dividend =3
return ans

#--------------------------------------------------------------
#TC-o(1)
'''same logic but we take i=32, 31, 30....till 0 to get it to - from dividend'''
def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    # sign
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0

    # check from highest bit → lowest
    for i in range(31, -1, -1): #o(32)-constant doesnt grow with the input size
        if dividend >= (divisor << i): # 15>=3x(2^32?.....till 2^2) first iteration
            dividend -= (divisor << i)# 15-3x(2^2), 15-12, dividend=3
            result += (1 << i)

    return result * sign