'''n = 39
coins=[10,5,2,1]
i=remain=count=0
while i <len(coins):
    if remain<=coins[i]:
        i+=1
        if n==0:
            break
    remain=n-coins[i] # but how will this continue subtracting?
    count+=1
print(count)'''

# for it to keep subtracting assign it to a value and decement it also make list of all inr denominations
coins=[2000,500,200,100,50,20,10,5,2,1]
n=39
total=n
m=0
result=[]
while total >0:
    if total>=coins[m]:
        result.append(coins[m])
        total-=coins[m] # keeps subtracting till least

    else:
        m+=1
print(len(result))
#o(1), o(n)
#or
total=n
m=count=0
while total >0:
    if total>=coins[m]:
        count+=1
        total-=coins[m] # keeps subtracting till least

    else:
        m+=1
print(count)
#o(1), #o(1)