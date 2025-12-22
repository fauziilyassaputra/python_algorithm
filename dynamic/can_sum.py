def can_sum(target_sum,number, memo=None):
    
    if memo is None:
        memo = {}
    # base case
    
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
        
    for num in number:
        reminder = target_sum - num
        if can_sum(reminder, number, memo) == True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False
    
print(can_sum(7,[2,3])) # True
print(can_sum(7,[5,3,4,7])) #True
print(can_sum(7,[2,4])) #False
print(can_sum(7,[2,3,5])) #True
print(can_sum(300,[7,14])) #False
