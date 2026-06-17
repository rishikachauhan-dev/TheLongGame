'''index 0 → try "("
index 1 → try "(" → "(("
index 2 → must close → "(()"
index 3 → close → "(())"

OR

index 1 → close → "()"
index 2 → open → "()("
index 3 → close → "()()"'''

#THe backtracking--Go deep → hit invalid → return → try next option for that index


class Solution:
    def solve(self,index,total,brackets,result):
        #base cases
        if index>=len(brackets):
            if total==0:
                result.append("".join(brackets))
            return
        
        #pruning-
        if total>len(brackets)//2:
            return # too many ( brackets need to stop for adding closing brackets
        
        if total <0: #invalid more closing brackets
            return
        #operation- choice 1
        brackets[index]="(" #not ) cuz invalid, if negative open that bracket
        sum=total+1
        #choice-1 ( for next
        self.solve(index+1,sum,brackets,result)

        #the backtrack is the overwriting after return in base case which means return to prev index

        #choice 2
        brackets[index]=")"
        sum=total-1
        self.solve(index+1,sum,brackets,result)  

    def generateParenthesis(self, n: int) -> List[str]:
        brackets=[""]*(n*2)
        result=[]
        # self.solve(0,0,'(',[])
        self.solve(0,0,brackets,result)
        return result

#Tc-2*n, Sc-n
'''
The solve function uses backtracking to build parentheses combinations while maintaining validity through the total parameter.
 The total keeps track of how many opening brackets are currently “unmatched” (waiting for their closing pair). 
 At each position, we try placing ‘(‘ (increases unmatched count) and ‘)’ (decreases unmatched count). 
 The key insight is the pruning: if total goes negative, we have more closing than opening brackets (invalid), 
 and if total exceeds n, we have too many unmatched opening brackets. When we fill all positions and total equals 0, all brackets are properly matched, so we add it to results
'''

'''CSN WRITE_
brackets[index] = "("
self.solve(index + 1, total + 1, brackets, result)

brackets[index] = ")"
self.solve(index + 1, total - 1, brackets, result)
'''