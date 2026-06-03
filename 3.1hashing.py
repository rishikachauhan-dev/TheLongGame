#Storing frequency dict.

num=[1,2,3,4,4,2,5,6,6,7,8,9,111]

freqmap=dict()
for i in range(0,len(num)): #0 # itll continue till the length nothing stops it
    if num[i] in freqmap: #1
        freqmap[num[i]]+=1 #1:2
    else:
        freqmap[num[i]]=1 #1:1
print(freqmap[4])
#Tc-o(n), SC = O(k) (≤ O(n)) Worst case (all different letters): SC = O(k) → O(n) if all are unique.
#But what matters for SC is how big it can grow with input.

# For storing characters
alph=['a','a','f','e','i','i','i','y','z','z']
freq_alpha={}
for c in range(0,len(alph)):
    if alph[c] in freq_alpha:
        freq_alpha[alph[c]]+=1
    else:
        freq_alpha[alph[c]]=1
if 'a' in freq_alpha: # change it inside code
    print(freq_alpha['a'])
else:
    print("not found")

##GFG:
arr=[1,2,3,4,4,2,5,6,6,7,8,9,111]

def findFrequency(arr, x):
    freq={}
    for a in range(0,len(arr)):
        if arr[a] in freq:
            freq[arr[a]]+=1 # return stops the iteration
        else:
                freq[arr[a]]=1
    return freq.get(x,0)
findFrequency(arr,x=1)
# freq = {1:2, 2:1, 3:1}
# freq[4] ❌ → KeyError# assumes the value is already there
# freq.get(4, 0) ✅ → 0 #cause .get() safely says:“If key 4 exists, give me its value.If not, just give me 0 (the default).”


