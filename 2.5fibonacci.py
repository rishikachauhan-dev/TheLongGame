#Fibonacci Seq
def fib(n=3):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2) # finds the 
print(fib())


#Optimized Tc-o(n), sc-o(n)


def fib1(n): # reversed 34 is the actual no. of 9
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1  # F(0), F(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print(fib1(9))
