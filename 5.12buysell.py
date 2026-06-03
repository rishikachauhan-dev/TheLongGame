prices=[7,2,1,5,6,4,8]
# prices=[8,5,3,2,1]
# min negative value which 2 numbers? but in ----> direction
maxi=float('-infinity')
for i in range(0,len(prices)): # B=i
    profit=0
    for j in range(i,len(prices)):#S=j
        profit=prices[j]-prices[i]
        maxi=max(maxi,profit)
if maxi<0: #o(1)
    print(0)
print(maxi)

#Tc=o(n^2)

#Optimal
minprice=float('infinity') # not -inf but inf for min// super max
maxprof=0 # for edge case this too
for i in range(0,len(prices)):
    minprice=min(minprice,prices[i]) # compare w/o if # if 2 <7 then ill buy at 2
    maxprof=max(maxprof,(prices[i]-minprice))
print(maxprof)



#revisin practise
prices=[7,2,1,3,6,4,9]
miprice=float('infinity')
maxp=0
for i in range(0,len(prices)):
    miprice=min(minprice,prices[i])# when to buy
    profit=(prices[i]-minprice)
    maxp=max(maxp,profit) #when to sell
print(maxp)
