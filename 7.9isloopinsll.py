#Brute

my_set=set() #=set() not () this is tuple
temp=head
while temp is not None:
    if temp in my_set:
        return True
    my_set.add(temp)
    temp=temp.next
return False

#o(n) sc-o(n)

#optimal
slow=head
fast=head
while fast is not None and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast: #this can only happen if there's a loop
        return True
return False

#o(n) sco(1)