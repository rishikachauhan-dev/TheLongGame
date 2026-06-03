nums=[5,7,8,4,1,6,9,2] 
#ascending order
n=len(nums)
for i in range (0,n):#index // 0...1
    min_indx=i #// 0
    for j in range(i+1,n):#  1...2..3..4..5..6..7
        if nums[j]<nums[min_indx]:#compare// 7<5?... 8<5?...4<5?..posibilty other nos. 1<4(i,j)..1<...
            min_indx=j # make j the min index // 3, 4 so 4 is the actaul min index then swap
    nums[i], nums[min_indx]=nums[min_indx],nums[i]# swap after j ends duh, //index 1(5),5(4)-5(4), 1(5)---#1,7,8,4,5,6,9,2  #min=4|1,2,8,5,4,6,9,7 iterate till u find the smallest value this happens as the min index keeps comparing with j+1(till n) as
print(nums)                                                                                               #min=7|1,2,8,5,4,9,7 #min=4|1,2,4,5,8,9,7 #min=7,5,8,4,2,7,9 #
                                                                                                            
#Tc-o(n(n+1/2))-o(n^2)-loop-1 itemation -j till end sc-o(1)

#descending
n=len(nums)
for i in range (0,n):#index,0
    max_indx=i
    for j in range(i+1,n):#1,2
        if nums[j]>nums[max_indx]:#compare 5-7-8
            max_indx=j # make j the max index j=1 max, 7 max
    nums[i], nums[max_indx]=nums[max_indx],nums[i]# swap after j ends duh

print(nums)

num=[5,7,8,3,1,6,9,2] 
num.sort()
print(num)
num.sort(reverse=True)
print(num)