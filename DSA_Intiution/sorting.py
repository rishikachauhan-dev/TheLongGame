# INSERTION #

# i,j,key

# arr[sorted | unsorted]

'''
'shift unsorted elements to right by finding right pos of key[i] comparing it with j which is just behind the i till n loop'

i loops till n and stores every value in key
j is just behind the i 
j compares value with key
when j>key
stop
now move every element to right till
j reaches the <=key
now the real pos of key is  j+1


loop till n
o(N)
o(1)
'''


#QUICK SORT#

#arr[low........high]

#arr[smaller | pivot | larger]

# arr[(low.... pivot)(pivot+1...high)]

'''
assign i=0 and j=len(n=arr)
low=i, high=j
make pivot=low                  first----can be middle, last

'comaparing i and j with pivot to swap elements left and right, then changing the pivot too by dividing arr to left and right each loop'

i++, j-- 
comparing each with pivot
when its not swap the values of i and j  
'this is to make sure pivot can have place in middle'
continue till they overlap-i<j

now smaller to left |pivot| larger to right
put the pivot in the correct pos
that is current j

cuz j is the at the end of the smaller side
swap it with pivot

recurse


(n//2)-pointers in each recurse gets divided into 2 arr
TC-N loop loop log2N for dividing 
nlogn
SC-1
'''

#MERGE SORT#

'''
[3,5,7,8,6,1,9,2]

'keep divide it into 2 arr till it gets individual element to compare'

then backtrack by comparing
i of arr1 and j of arr2
compare each and store them in temp=[]
then repalce it i=with original arr-inplace


logn for dividing by 2 each time
n/2+n?2 for i and j

nlogn
o(n)

'''

#SELECT SORT#
'''
i,j,min_ind

i=0
min_ind=arr[0]
' for each i comapre j with curr min index'



for i till n 
    j=1 till n
    compare j with curr min_index
    then swap it
now start another loop from i=1 till n and min_index=arr[1]

o(n^2)

'''

#BUBBLE sort
'''
swap elements i and i+1 by comparing each till j 

here the largest unsorted element gets sorted first
j-- 
cuz no point of comparing the last sorted element


o(n^2) cuz 2 loop one for j-- then for each 
j-- i and i+ swap loop till j
o(1)
'''