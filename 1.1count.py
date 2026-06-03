##my logic--

# n=(input("Enter: "))
# count=len(n)
# print(count) #TC=O(1) SC=O(1) len()-O(1)

##math logic
n=int((input("Enter no.: ")))#543
num=n
count=0
while num>0:
    # num%10 #3 dont need its extra
    num=num//10#54 #update it 
    count+=1
print(count) #TC=O(log10 n) can say log n too cuz base 10 is written this way cuz dividing by 10 SC=O(1)

    

