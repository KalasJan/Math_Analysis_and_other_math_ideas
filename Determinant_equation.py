# Solve the determinant equation
# M = ([
    # [x, 1, 2],
    # [1, x, 2],
    # [1, 2, x]])
    
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
n = 1
              
M = sp.Matrix([
    [x, 1, 2],
    [1, x, 2],
    [1, 2, x]
])

# 1) Count the determinant
detM = M.det()
print (f'Determinant is {detM}')

# 2) finding roots
roots = sp.solve(detM - n, x)
print (f'Root is (roots are) {roots}')

# 3) plot the polynom as a graph - only real roots (not complex)
f_det = sp.lambdify(x, detM, 'numpy')

real_roots = []
for r in roots:
    val = r.evalf()
    # if the root is real
    if val.is_real:
        real_roots.append(float(val))

# real roots  or complex on interval (-5, 5)
if real_roots:
    axx = np.linspace(min(real_roots) - 1, max(real_roots) + 1, 500)
else:
    axx = np.linspace(-5, 5, 500)

axy = f_det(axx)


plt.figure(figsize=(9, 5))
plt.plot(axx, axy, color='darkblue', lw=2, label='f(x) = det(M)')

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

plt.axhline(n, color='red', linestyle=':', label=f' f(x) = {n}')

plt.title('Graph of polynom det(M)')
plt.xlabel('x')
plt.ylabel('det(M)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

# 4) Working with roots
# x1 + x2 + x3 + ...
sum_roots = sum(roots)
print (f' Sum of roots is {sp.simplify(sum_roots)}')

# x1^2 + x2^2 + x3^2 + ...
sum_suqare = sum(r**2 for r in roots)
print (f' Sum of squares of roots is {sp.simplify(sum_suqare)}')

# x1 * x2 * x3 * ...
prod_roots = 1
for r in roots:
    prod_roots *= r
print(f'Product of roots is {sp.simplify(prod_roots)}')