# Head Recursion

# count=0-was treated a global var ciz its
def greet(count=0):
    if count==4:
        return
    print("Hi")
    greet(count+1)
greet()

#Tail Recursion
def greet1(count=0):
    if count==4:
        return
    greet1(count+1) # calling line 12 here again
    print("Hehe")
    
greet1()