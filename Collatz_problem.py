# Collatz problem

def collatz(n):
    sequence = [n]
    
    while n > 1:
        if n  % 2 == 0:
            n = n // 2 # n is even
        else:
            n = 3*n + 1 # n is odd
        sequence.append(n)
    
    return sequence

n = int(input('Write the value of n = '))

result = collatz(n)

m = len(result)

print(f' The Collatz sequence for n = {n} has {m} terms: ', ' - '.join(map(str, result)))
