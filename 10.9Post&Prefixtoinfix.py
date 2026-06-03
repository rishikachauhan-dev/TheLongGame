#PostfixtoInfix

class Solution:
    def postToInfix(self, postfix):
        stack=[]
        
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            else:
                operand2=stack.pop() #debugged was opreand 1 should be 2 cuz the second element will pop first
                operand1=stack.pop()
                
                newexp=f"({operand1}{char}{operand2})"
                stack.append(newexp)
                
        return stack[-1] #final list of the element is the result
#o(n)
#o(n)

#PrefixToInfix
class Solution1:
    def preToInfix(self, pre_exp):
        stack=[]
        for char in pre_exp[::-1]:
            if char.isalnum():
                stack.append(char)
            
            else:
                operand1=stack.pop()
                operand2=stack.pop()
                
                newexp=f"({operand1}{char}{operand2})"
                
                stack.append(newexp)
        return stack[-1]   
#o(n)
#o(n)