#Head
def funct1(i,n):
    if i>n:
        return
    print(i)
    funct1(i+1,n)
funct1(1,4)

#Tail-N to 1
def funct(i,n):
    if i>n:
        return
    funct(i+1,n)
    print(i)

funct(1,5)

#N to 1 Head
def funct2(n):
    if n==0:
        return
    print(n)
    funct2(n-1)
funct2(8)

#1 to N Tail
def funct3(i,n): #1,4 2,4 4,4 5,4
    if i>n:#no
        return
    funct3(i+1,n)#2,4.. 3,4.. 4,4
    print((n-i)+1)
funct3(1,4)