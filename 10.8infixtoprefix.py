'''
| Conversion                     | `^` behavior             |
| ------------------------------ | ------------------------ |
| Infix → Postfix                | right associative        |
| Infix → Prefix (after reverse) | behaves left associative |

same code
but
char == '^'

w/o ---- stack and 
                    (self.precedence(stack[-1])>self.precedence(char)
                    or
                    (self.precedence(stack[-1])==self.precedence(char)))):
                    result.append(stack.pop())

[+, -, ^]

If ^ exits early:

[+, -]

Now who becomes front/top changes.
'''
s="(a+b)+c^d^e"
class Solution:
    def precedence(self,c):
        if c=='+' or c=='-':
            return 1
        if c=='*' or c=='/' or c=='%':
            return 2
        
        if c=='^':
            return 3
            
        return 0
            
    def infixToPrefix(self, s):
        s=s[::-1] #reverse the string
        #replace the brackets
        s=s.replace("(","temp").replace(")","(").replace("temp",")")
        stack=[]
        result=[]
        #infix to postfix
        for char in s:
            if (('a'<=char<='z') or
                ('A'<=char<='Z') or
                ('0'<=char<='9')):
                    result.append(char)
                    
            elif char=='(':
                stack.append(char)
                
            elif char==')':
                while stack and stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
                
            else:
                while (
                    stack and 
                    (self.precedence(stack[-1])>self.precedence(char)
                    or
                    (self.precedence(stack[-1])==self.precedence(char) and char=='^'))):
                    result.append(stack.pop())
                stack.append(char)
                
        #remaining
        while stack:
            result.append(stack.pop())
        #now reverse again it will be prefix
        # return ''.join(result[::-1])
        print(''.join(result[::-1]))
'''
TC
String reversal takes O(n) time.
Parenthesis swapping takes O(n) time.
The infix to postfix conversion part takes O(n) time, with each character pushed and popped at most once.
Final result reversal takes O(n) time.
Overall, the time complexity is linear in the length of the input string.

Space Complexity: O(n)
The reversed input string requires O(n) space.
The stack might store up to O(n) characters in the worst case.
The result list will eventually store O(n) characters.
Therefore, the space complexity is linear in the length of the input string.
'''