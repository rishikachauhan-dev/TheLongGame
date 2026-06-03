#1,n
num=int(input())
for n in range(1,num+1):
    if num%n==0:
        print(n)
    else:
        continue  #T=o(n)


# Optimized Concept
# Instead of looping till n, you only need to check till √n:
# If i divides n, then both i and n//i are factors.
# Example: For n=36, checking till √36=6 is enough:
# 1 × 36
# 2 × 18
# 3 × 12
# 4 × 9
# 6 × 6

class Solution:
    def countFactors(self, n: int) -> int:
        count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i * i == n:   # perfect square
                    count += 1
                else:
                    count += 2   # i and n//i
            i += 1
        return count
# T=o(root(n))



# 1️⃣ Problem: Count factors of a number n
# Factors = numbers that divide n exactly (no remainder).
# Example:
# Factors of 20 → {1, 2, 4, 5, 10, 20}
# Factors of 36 → {1, 2, 3, 4, 6, 9, 12, 18, 36}

# 2️⃣ Naive way (your first code)
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1


# 👉 Check every number from 1 to n.
# For n=20, that’s 20 checks.
# For n=1,000,000,000, that’s 1 billion checks ❌ → too slow.

# 3️⃣ Smarter observation

# 👉 Factors come in pairs.
# If i is a factor, then n // i is also a factor.
# Example: n = 20
# 1 divides 20 → partner factor = 20 // 1 = 20
# 2 divides 20 → partner factor = 20 // 2 = 10
# 4 divides 20 → partner factor = 20 // 4 = 5
# So by checking only small numbers, we also discover their big partners.

# 4️⃣ Why stop at √n?

# If we go beyond √n, we’re just repeating factor pairs we already found.
# For n=20:
# √20 ≈ 4.47 → we only check 1, 2, 3, 4.
# At i=1 → (1, 20)
# At i=2 → (2, 10)
# At i=3 → not a factor
# At i=4 → (4, 5)
# 👉 Done! We found all factors.

# No need to check 5, 10, 20 again because they already appeared as partners.
# 5️⃣ Special case: perfect square
# For n=36:
# At i=6, partner is 36 // 6 = 6 (same number).
# If we counted both, we’d double-count 6.
# So in that case, we only add 1.

# 6️⃣ Algorithm in plain English
# Start count = 0.
# Loop i from 1 to √n.
# If i divides n:
# If i * i == n: add 1 (perfect square).
# Else: add 2 (i and n//i).
# Return count.

# 7️⃣ Example Walkthrough with n = 20
# i = 1 → divides → add 2 → count = 2 (factors: 1,20)
# i = 2 → divides → add 2 → count = 4 (factors: 2,10)
# i = 3 → doesn’t divide → skip
# i = 4 → divides → add 2 → count = 6 (factors: 4,5)
# Loop ends (i² > 20).

# ✅ Total factors = 6.

# i till √n only used to count
n=int(input("-"))
i=1
count=0
while i*i<=n:
    if n%i==0: 
        # n//i no neet direct count as 2
        if n==i*i:
            count+=1
        else:
            count+=2   
    i+=1  # i need inc after i=1
print(count) 



## Aproach
n=int(input())
count=0
for i in range (1, n//2):
    if n%i==0:
        count+=1

count+=1
print(count) 
#TC-o(log2(n)) SC-o(1)
# Aha 🔥 nice observation! You’re mixing two different algorithms here:
# Counting digits → num // 10 each step → logarithmic.-variable ko jitne se km krte ho loop mei
# Counting factors (divisors) → for i in range(1, n//2) → linear. SO here TC-o9=(n/2)-o(n)



