five=ten=0
for i in range(len(bills)):
    if bills[i]==5:
        five+=1
    elif bills[i]==10:
        if five>=1: # do we have chnage
            five-=1
            ten +=1 # can only take if we have chnage
        else:
            return False
    else: # bills[i]==20:
        # 2 cond- 1-10 1 5 or 3 five notes
        if ten>=1 and five>=1: # both must me true
            ten-=1
            five-=1
        elif five>=3:
            five-=3
        else:
            return False
return True

#o(n)
#o(1) on;y five and ten used