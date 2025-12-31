# def countConstruct(target, wordBank):
#     if target == '':
#         return 1
    
#     totalCount = 0
    
#     for word in wordBank:
#         if target.startswith(word):
#             numWaysForRest = countConstruct(target[len(word):], wordBank)
#             totalCount += numWaysForRest
            
#     return totalCount
    
def countConstruct(target, wordBank, memo=None):
    if memo == None:
        memo = {}
    
    if target in memo:
        return memo[target]
    
    
    if target == '':
        return 1
    
    totalCount = 0
    
    for word in wordBank:
        if target.startswith(word):
            numWaysForRest = countConstruct(target[len(word):], wordBank, memo)
            totalCount += numWaysForRest
    
    memo[target] = totalCount
    return totalCount
    
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) 
