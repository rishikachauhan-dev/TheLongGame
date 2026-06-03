# Set Matrix Zeros
'''matrix[row][col] eg. arr=[[1,2,3],[4,5,6]] here matrix[2][3], r=len(matrix), c=len(matrix[0])


brute -----
a function call, if matrix[i][j]!=0,
2 loops for i in matrix and j in matrix till each end, put
infi in that row and col keeping matix[i][j++], then matrix[i++][j]
then call function to replace it with infinity
where there is infi replace it with 0

o((m * n) * (m + n)), o(1)
For each zero, we may mark an entire row and column

better------
1 row track list, 1 col track list
for i in range(row) and j till col,  rowTrack = [0 for _ in range(r)]
when matrix[i][j]==0, -1 on each track,
then replace where rowtrack[i]==-1 or coltrack[j]==-1 to matrix[i][j]=0

o(mxn)+n, o(m+n)

optimal
frist col and row as matrix 1 col/row extra as boolean-T/F, flag the particular row/col to be zeroed fro 1 loop of i in r and j in c,
then skip firt row/col, then turn it to 0

then for t/f do flag it to 0

o(nxm)
o(1)
'''
# 3sum
'''
arr=[] sum=0

brute
arr[k]=arr[i]+arr[j] for every i and j pair

o(n^2)

optimal
sort arr
arr[i] i++ starts from k+1, arr[j] j--, arr[k]=loop of k from 0 to n
k+i+j=0 >0 j--, <0 i++
add triplest to result
if k==k-1 continue

o(n)
o(triplets)

'''