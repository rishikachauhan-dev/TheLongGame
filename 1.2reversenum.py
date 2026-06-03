#My logic

# n=input()
# num=n[::-1] #n.index('5')
# print(num)


##Math logic
n=int(input())#543
rev=0
while n>0:
    num=n%10#3
    n=n//10#54
    rev=(rev*10)+num #so 3 got restored in rev since 0
print(rev) #TC=o(n) SC-o(1)
