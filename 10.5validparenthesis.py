class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for bracket in s:
            '''if (bracket=='('or bracket=='{' or bracket=='['):
                stack.append(bracket) # in string no append'''
            if bracket in "([{":
                stack.append(bracket)
            else: #means in iteration there's a closing  bracket
                if len(stack)==0: #if closing bracket showed up and stack still empty means no pair
                    return False
                pair=stack.pop()
                if (
                    (pair=='(' and bracket==')') or
                    (pair=='{' and bracket=='}') or
                    (pair=='[' and bracket==']')
                ):
                    continue
                else: #if mismatch pair={ and bracket=] 
                    return False

                #if stack all did not pop means pair was not found so False else True
        return len(stack)==0

''' 
the mismatch part is after opening bracket it will expect a close one for the last one the LIFO
{ [ ( ] ) } invalid
{()[]} valid cuz in stack opening will be in top of e/o so the next closing element will expect

edge cases
1. s empty 
2. stack empty for closing pair
3. mismatch
4. s empty but stack left

Tc-o(n), o(n)
'''
# closing → opening
# “What opening bracket should ')/ch' match?”
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # mapping closing -> opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # opening bracket
            if ch in "({[":
                stack.append(ch)

            # closing bracket
            else: # closing bracket-"()"
                # stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]: # key-> value
                    '''if stack empty or 
                    top of stack == mapping[key of closing braket]?'''
                    return False

                stack.pop()

        # valid only if stack becomes empty
        return len(stack) == 0


# reverse lookup
'''Suppose:
stack[-1] = '('
You want to find:
Which key has value '(' ?
Dictionary:
')' : '('
So answer should be:
')' '''
class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for bracket in s:

            if bracket in "({[":
                stack.append(bracket)

            else:

                if not stack:
                    return False

                pair = stack.pop()

                expected = "" #place holder for 

                # reverse search
                for key, value in mapping.items():

                    if value == pair:

                        expected = key
                        break

                if bracket != expected: #mismatch
                    return False

        return len(stack) == 0
'''
⚡ Final takeaway
Operation	Complexity
key → value	O(1)
value → key	O(n) loop needed

Because dictionary optimized for:

✅ key lookup only'''