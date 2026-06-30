start= [1, 3, 0, 5, 8, 5]
finish= [2, 4, 6, 7, 9, 9]


'''
N Meetings in One Room

1. Pair (end,start)
2. Sort by END time
3. Take first meeting
4. If start > last_end:
       take meeting
5. Count selected meetings

Greedy:
"Finish earliest, leave room for others.---jo meeting jldi khtm ho rhi hai use pehle lo zyda meeting le paoge room mei"
'''
class Solution:
    def activitySelection(self, start, finish):
        #code here
        meeting=[]
        for i in range(len(finish)):
            meeting.append((finish[i],start[i]))
        
        meeting.sort()# to sort by end take end first in the meeeting
        # meeting =[(2, 1),(4, 3),(6, 0),(7, 5),(9, 5),(9, 8)]
        count=1
        lastend=meeting[0][0]
        
        for i in range(1,len(finish)):
            currstart=meeting[i][1] #(0,1), (0,1), row[col], # meeting[list][tuple mei konsa element]
            currend=meeting[i][0]
            
            if currstart>lastend:
                count+=1
                lastend=currend
            # else:
            #     pass, without is behaves the same way
        return count
    
#o(nlogn)-sort used 
#o(n)