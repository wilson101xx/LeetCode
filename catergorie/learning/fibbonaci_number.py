

def fib(nth):
    
    #base case is 1
    if nth <= 1:
        return nth
    
    return (fib(nth-1) + fib(nth-2))

print(fib(40))