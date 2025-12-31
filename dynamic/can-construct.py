# def can_construct(target, wordBank):
#     if target == "":
#         return True
        
#     for word in wordBank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             if can_construct(suffix, wordBank) == True:
#                 return True
    
#     return False

def can_construct(target, wordBank, memo=None):
    if memo == None : 
        memo = {}
    
    if target in memo:
        return memo[target]
    
    if target == "":
        return True
        
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False
    
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False
