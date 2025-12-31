# def howSum(target_sum, numbers):
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
        
#     for num in numbers:
#         remainder = target_sum - num
#         remainderResult = howSum(remainder, numbers)
#         if remainderResult is not None:
#             return remainderResult + [num]
            
#     return None
    
def howSum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
        
    for num in numbers:
        remainder = target_sum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            memo[target_sum] = remainderResult + [num]
            return memo[target_sum]
            
    memo[target_sum] = None        
    return None

print(howSum(7,[2,3])) # [3,2,2]
print(howSum(7,[5,3,4,7])) # [4,3]
print(howSum(7,[2,4])) # None
print(howSum(8,[2,3,5])) # [2,2,2,2]
print(howSum(300,[7,14])) # None
