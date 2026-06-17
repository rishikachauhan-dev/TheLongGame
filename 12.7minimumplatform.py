arr = [900, 940, 950, 1100, 1500, 1800]
dep= [910, 1200, 1120, 1130, 1900, 2000]

#Brute
maxi=1
for i in range(0, len(arr)): # both arr and dept treat as a block
    count=1
    for j in range(i+1,len(arr)):
        if arr[j]< dep[i]:
            count+=1

    maxi=max(maxi,count)
print(maxi)

#Tc-o(n^2)

#Optimal
'''sort both then iterate for arr and dep, count+1 for arr -1 for dep'''

# arr=arr.sort()
# dep=dep.sort() this for new sorted list

arr.sort()
dep.sort()

count=platform=1# 1 platform needed by default
i=1 # assuming first train already arrived, we will compare j with the next arrival
j=0
while i< len(arr) and j<len(dep):
    if dep[j]<arr[i]: # means dep before arr of i no need for new platform, dep jldi ho rha, for gfg needs new platform if equal arr and dep
        count-=1
        j+=1 # see or dep jo jldi ho rhe hai
        
    else: # arrival hai
        count+=1
        i+=1 # if more arrivals
    platform=max(platform, count) # the max count was the platform needed
return platform

#Tc-nlogn+n+n cuz i j moving separately?--nlogn overall
#Sc-o(1)


