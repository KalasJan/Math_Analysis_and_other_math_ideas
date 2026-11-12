# Special numbers and series

n = int(input('Write the value of n = '))

interval = range(1, n+1)

# triangle number
def Triangle(n):
    return [i * (i+1)//2 for i in interval]

t_seq = Triangle(n)

# square numbers
def Square(n):
    return [i **2 for i in interval]

s_seq = Square(n)

# pentagonal numbers
def Pentagonal(n):
    return [i*(3*i-1)//2 for i in interval]

p_seq = Pentagonal(n)

# hexagonal numbers
def Hexagonal(n):
    return [2*i**2 - i for i in interval]

h_seq = Hexagonal(n)

print(f"\nFor n = {n}:")
print("Triangles:  ", " - ".join(map(str, t_seq)))
print("Squares:    ", " - ".join(map(str, s_seq)))
print("Pentagonal: ", " - ".join(map(str, p_seq)))
print("Hexagonal:  ", " - ".join(map(str, h_seq)))