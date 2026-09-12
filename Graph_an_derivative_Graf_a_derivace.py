# plot the function f(x) = x * np.sin(x), 1st and 2nd derivative

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x = sm.Symbol('x')

# functions
y = x * sm.sin(x)
y_num = sm.lambdify(x, y, 'numpy')

dx = sm.diff(y, x)
dx_num = sm.lambdify(x, dx, 'numpy')

dxx = sm.diff(dx, x)
dxx_num = sm.lambdify(x, dxx, 'numpy')

# tangent on function
x0 = 1
y0 = y_num(x0)

der = float(dx.subs(x, x0).evalf())
norm = -1 / der

tang_gr = der * (x - x0) + y0
norm_gr = norm * (x - x0) + y0

tang_sim = sm.simplify(tang_gr).evalf(3)
norm_sim = sm.simplify(norm_gr).evalf(3)

tangent = sm.lambdify(x, tang_sim, 'numpy')
normal = sm.lambdify(x, norm_sim, 'numpy')

# titles
y_latex = sm.latex(y)
dx_latex = sm.latex(dx)
dxx_latex = sm.latex(dxx)

# graphs
t = np.linspace(-2 * np.pi, 2 * np.pi, 500)
t2 = np.linspace(x0 - 2, x0 + 2, 5)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 10), sharex=True)

# 1) f(x)
ax1.plot(t, y_num(t), label = 'Function', color='red')
ax1.plot(t2, tangent(t2), label = 'Tangent', color='Green', linestyle='--')
ax1.plot(t2, normal(t2), label = 'Normal', color='Blue', linestyle=':')

ax1.scatter(x0, y0, label=f'Point [{x0}, {y0:.2f}]', color='black', s=40, zorder=5)

ax1.set_ylabel('y')
ax1.set_title(f'$f(x) = {y_latex}$')
# ax1.set_aspect('equal', adjustable='box')
ax1.legend()
ax1.grid(True)

# 1st derivative
ax2.plot(t, dx_num(t), color='saddlebrown')
ax2.set_ylabel('y')
ax2.set_title(f'$f\'(x) = {dx_latex}$')
ax2.grid(True)

# 2nd derivative
ax3.plot(t, dxx_num(t), color='Purple')
ax3.set_ylabel('y')
ax3.set_title(f'$f^{(2)}(x) = {dxx_latex}$')
ax3.grid(True)

plt.tight_layout()
plt.show()