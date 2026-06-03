#Parametrized

def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)

func(0,1,4)

# print
def func1(sum,i,n):
    if i>n:
        # print(sum)
        return
    print(sum)
    func1(sum+i,i+1,n)

func1(0,1,5)


# Functionalised

def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)

print(fun(4))