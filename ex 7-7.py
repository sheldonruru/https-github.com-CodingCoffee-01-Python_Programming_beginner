def factoria(n):
    if n == 1:
        return 1
    #else:
        #print(n)
    return n * factoria(n - 1)
    
print(factoria(5))
