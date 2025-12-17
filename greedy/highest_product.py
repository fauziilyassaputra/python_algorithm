def highest_product(A):
    A = sorted(A)
    
    hi3 = A[-1] * A[-2] * A[-3]
    low2h1 = A[0] * A[1] * A[-1]
    
    return max(hi3, low2h1)
    
test = [0,1,2,3,4,5]
print(f"result 1 - 5 : {highest_product(test)} ")

test2 = [-5, -3,0,1,2,3]
print(f"result -5 - 3: {highest_product(test2)}")
