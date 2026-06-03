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

        #operation
        brackets[index]="(" #not ) cuz invalid
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