n=int(input("-"))
i=2
str=''
while i*i<=n: # n//2 takes longer #root n is much faster as all divisors/factors will show up before that
    if n%i==0:
        str='Not Prime'
        break
    i+=1
    if i*i>=n:
        str='Prime'
    
print(str)     
 
#Brute---
n=int(input())
for i in range(2, n//2):
    if  n%i==0:#10/2=5 so idhr himpta chl gya ki composite h to aage check krne ki zarurat nhi
        print('Not')
        break # breaks loop only then next line inside thin loop will not work
    # if i==(n//2)-1:
    #     print('prime')
    else:
        print('prime')

    
