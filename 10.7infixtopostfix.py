class Solution:
    def precedence(self,c):
    #hirarchy
        if c=='+' or c=='-':
            return 1
        
        if c=='*' or c=='/':
            return 2
        
        if c=='^':
            return 3
        
        return 0
     
    def infixtoPostfix(self, s):
        stack=[]
        result=[]
        
        #oprand
        for char in s:
            if (('a'<=char<='z') or ('A' <=char<='Z') or 
            ('0'<=char<='9')):
                result.append(char)
            
            elif char=='(':
                stack.append(char)
                
            elif char==')':
                while stack and stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop() #cancels it out
            
            else: #if operator here stack char lower-higher priority
                while(
                    stack and
                        (self.precedence(stack[-1])>self.precedence(char)
                        or 
                        (self.precedence(stack[-1])==self.precedence(char) 
                        and char!='^'))):
                        result.append(stack.pop()) #push it to result
                stack.append(char) #else default puch into stack
            
            #after all this push stack in append now the result will have higher priority first
        while stack:
            result.append(stack.pop())
        
        return "".join(result) #convert list to string

            
#o(n), o(n)
''' the simplified bracket thing
stack exists
AND
(
higher precedence
OR
(equal precedence + not ^)
)
'''
'''
why failed?
For ^:

equal precedence should NOT pop
Only STRICTLY greater precedence should pop.
| Operator  | Associativity |
| --------- | ------------- |
| `+ - * /` | Left to Right |
| `^`       | Right to Left |

Why separate > and ==?
Because:
greater precedence ALWAYS pops
but:
equal precedence depends on associativity

| Case                              | Decision  |
| --------------------------------- | --------- |
| top stronger than current         | pop       |
| same strength + left associative  | pop       |
| same strength + right associative | don't pop | means A^B^C old ^ vs new ^


'''