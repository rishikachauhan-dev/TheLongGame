#PreToPost
class Solution:
    def preToPost(self, s):
        # Code here
        stack=[]
        for i in range(len(s)-1,-1,-1): #Reverse iteration
            char=s[i]
            if char.isalnum():
                stack.append(char)
            
            else:
                operand1=stack.pop()
                operand2=stack.pop()
                
                newexp=operand1+operand2+char
                
                stack.append(newexp)
        return stack[-1]
#0(n)
#0(n)

#PosttoPre
class Solution:
    def preToPost(self, s):
        # Code here
        stack=[]
        for char in s:
            if char.isalnum():
                stack.append(char)
            
            else:
                operand2=stack.pop()
                operand1=stack.pop()
                
                newexp=f"{char}{operand1}{operand2}"
                
                stack.append(newexp)
        return stack[-1]
#o(n)
#o(n)