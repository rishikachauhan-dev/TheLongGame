#Brute--
len=0
temp=head
while temp:
    len+=1
    temp=temp.next
    # return len # will count 1 loop
# return len #will stop the whole code to return only this

if len-n==0:
    head=head.next
    # del head #optional
    return head
temp=head
m=len-n
# count=1
# while count<m:
#     temp=temp.next
#     count+=1
# temp.next=temp.next.next
for _ in range(0,m):
    temp=temp.next 
temp.next=temp.next.next 
return head

#.......................................LEETCODE
length = 0
temp = head

while temp:
    length += 1
    temp = temp.next

# delete head case
if length - n == 0:
    return head.next

temp = head
m = length - n

for _ in range(m - 1):   # stop before node
    temp = temp.next

temp.next = temp.next.next
return head

#TC-o(2n)~o(n)

#optimal-----
slow=head
fast=head
for _ in range(n): #boost will maintain the gap b/w slow and fast so when fast ends with 1 step slow reaches the index-1 point
    fast=fast.next

if fast is None: # if n>len of node means del head cuz del from end
    return head.next 

while fast.next is not None: # we want index-1 to connect it to 3rd deleting 2nd
    slow=slow.next
    fast=fast.next # after boosting its step is by 1
#deleting
slow.next=slow.next.next
return head