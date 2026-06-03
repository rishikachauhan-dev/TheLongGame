#x, n times
#usually solved with parameters, always dry run with tree

def func(x,n): #
    if n==0:
        return #base condition
    print(x)
    func(x,n-1)

func(14,4)

def func1(x,n): #Tail
    if n==0:
        return #base condition
    func1(x,n-1)
    print(x)

func1(13,5)