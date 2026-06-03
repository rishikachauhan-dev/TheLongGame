#Hashing

#store freq using brute force
n=[5,3,4,7,7,2,5,8,9,10,8]
m=[11,56,34,5,7,8,1,3]

def hash():
    for i in m: # check j repeated how many times in n
        count=0
        for j in n:
            if j==i:
                count+=1
        print(i,count) #print(count) is outside the inner loop, You reset count=0 for each i in m. After finishing the loop, only the last value of count is printed (not all counts).
hash()

#Tc-o(nxm) sc-o(1) but n-10^8 m-10^8=10^16 TLE

#Prestoring
# m jo numbers h wo n mei kitne baar repeated h within constraints
#input expected a no. otput its frequncy

hash_list = [0] * 11   # store counts for numbers 1..10

# O(n)
for num in n:   # only count within constraints
        hash_list[num] += 1# adding freq cuz initially 0 with no. matching with index so if already 1->+1=2
# O(m)
for num in m: #  num can be used cuz out of scope-loop variable
    if 1 <= num <= 10:       # valid lookup
        print(hash_list[num]) # if within constraints print the haslist index num-will have the frequncy
    else:
        print(0)
#T=o(n+m) #S=o(n)

#n=[1,2,3,4,1,2,3,4,5,7,1,8] i /num
#hashlist=[0,2,1,0,0,0,0,0,0,0,0]#0,1,2,3,4,5,6,7,8,9,10
#m=[1,20,5,2] j / num
#hash[j]=print=2
#m<1 or10> print=0
