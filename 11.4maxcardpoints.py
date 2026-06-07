cardPoints = [1,2,3,4,5,6,1]
k = 3
# Output: 12

#Brute-for every i iterate j to add count to k and store max
#----
cardPoints =[100,40,17,9,73,75]
k =3 #TC failed-expected-248, 157
'''
right=left=total=count=maxi=0

while right< len(cardPoints):
    
    total+=cardPoints[right]
    count+=1
    if count>k:
        total-=cardPoints[left]
        count-=1
        left+=1 # debugged 3x indentation, element increment instead of index
    maxi=max(total,maxi) # tc failed addes this---still failed
    right+=1
print(maxi)
#o(n)
#o(1)'''

left=total=count=0
right=len(cardPoints)-1
'''left>rigth left++ else right++ till count=k, equal add left right --'''
'''
if k==len(cardPoints):
    return sum(cardPoints)
while left<=right and count<k:
    if cardPoints[left]>cardPoints[right]:
        total+=cardPoints[left]
        left+=1
        count+=1
    elif cardPoints[left]<cardPoints[right]:
        total+=cardPoints[right]
        right-=1
        count+=1
    else:
        total+=cardPoints[left]
        left+=1
        right-=1
        count+=1
print(total)'''
#TC failed here too
#------------
n=len(cardPoints)
if k==n:
    print(sum(cardPoints))
ls=rs=maxi=0
#all from start
for i in range(0,k):
    ls+=cardPoints[i]
maxi=ls #first left
rindex=n-1
#take from ends and - from start
for i in range(k-1,-1,-1):
    ls-=cardPoints[i]
    rs+=cardPoints[rindex]
    maxi=max(maxi,ls+rs)
    rindex-=1 #decremeant right
print(maxi)
#o(k)-worst, o(2n)
#o(1)