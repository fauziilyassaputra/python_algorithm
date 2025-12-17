def bulbs(A):
    cost = 0
    
    for i in A:
        if cost % 2 == 0: 
            if i == 0:
                cost += 1
        
        if cost % 2 == 1:
            if i == 1:
                cost += 1
        
        
    return cost
    
test = bulbs([0,1,1,0,0,1,0,0,1,0])
print(test)
