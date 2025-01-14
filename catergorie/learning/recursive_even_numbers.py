

def evenNums(num):
    if num % 2 != 0:
        return "Odd"
    if num <= 2:
        return num
    
    return evenNums(num-2)

print(evenNums(990))