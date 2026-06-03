class Solution:
    def solve(self,ind,subset,result,digits):
        charmap={
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",}

        #base case
        if ind>=len(digits):
            result.append("".join(subset)) #.copy()-wrong cuz it contains char 
            return
        if digits=="":
            return
        #operation
        for ch in charmap[digits[ind]]: #[] for dic not-charmap(digits[ind])
            subset.append(ch)
            self.solve(ind+1,subset,result,digits)
            
            #backtrack
            subset.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        self.solve(0,[],result,digits)
        return result
    
'''
.join vs copy----------

Core difference:
Method	    Purpose
.copy()	    duplicate a mutable object
"".join()	convert list of strings into ONE string

'''