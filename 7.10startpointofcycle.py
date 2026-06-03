#Brute
myset=set()
    temp=head
    while temp is not None:
        if temp in myset:
            return temp
        myset.add(temp)
        temp=temp.next


#Optimal
slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow