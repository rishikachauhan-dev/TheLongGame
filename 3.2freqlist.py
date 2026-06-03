# create a freq list og the given arr with as m=[index 0 if not there] for n

n=[1,3,4,4,5,6,8]
# count=0
# new=[]-> i indexing

a=max(n) #len(n)+1---> this will take the length of the n list not the largest element in it we want the largest element so that it can match with new list index
new=[0]*a # max=largest element in n+1
for i in n:
    new[(i-1)]+=1
print(new)


##Gfg
arr=[1,4,5,6,7,3,4,5,6,] # ques 1-n
n=len(arr)
new=[0]*n
for i in arr:
    new[i-1]+=1
print(new)