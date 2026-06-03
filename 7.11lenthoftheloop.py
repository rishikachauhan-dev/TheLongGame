#Brute--

#instead of set use dict to store the travel with the node, then last temp travel-if temp in dict found's travel
mydict={}
travel=0
temp=head
while temp is not None:
    if temp in mydict:
        return travel-mydict[temp] #the index difference
    mydict[temp]=travel #adding travel as a value to the node which is key
    travel+=1
    temp=temp.next
return 0 #if no loop

#o(n) sc-o(n)

#optimal---
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
if slow==fast: # start counting from here
    slow=slow.next
    count=1
    while slow!=fast: # loop s again till its == f, travel+=1
        slow=slow.next
        count+=1
    return count

return 0