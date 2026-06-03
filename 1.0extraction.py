##my logic
# n=input()
# for i in n:
#     print(i) #TC o(n) SC-o(1)


n=int(input("No.: "))
while n>0:
    num=n%10
    n=n//10
    print(num) #TC-o(n) SC-o(1)