def factoria(n):
    if n == 1:
        return 1
    else:
        print(n)
    return factoria(n - 1)
    
print(factoria(3))
