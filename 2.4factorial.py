class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        def fun(n):
            if n==1:
                return 1
            return n*fun(n-1)
        return fun(n)


# If?

def factorial(self, n: int) -> int:
        def fun(n):
            if n==1:
                return 1
            return n*(n-1)
        return fun(n)


# ❌ Problems
# Wrong recursive formula
# You wrote:
# return n * (n - 1)


# This only multiplies two numbers once.
# For example: fun(5) → 5*4 = 20 (not 120).
# Factorial requires recursion:
# n!=n×(n−1)!

# No recursive call
# Instead of calling fun(n-1), you’re just subtracting.
# That breaks the recursion chain.