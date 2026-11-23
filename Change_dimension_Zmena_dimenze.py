# Zmena dimenze
# R2 -> R2 je v dokumentu Zmena_baze
# R -> R2 je v Graf_parametricky

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, z = sp.symbols('x y z')

# 1) Obecne R2 -> R3

# a) definice
u = x+y
v = x*y
w = x**y

F = sp.Matrix([u, v, w])
X = sp.Matrix([x, y])

# b) Jacobian
J = F.jacobian(X)
print("Jacobiho matice zobrazení R^2 -> R^3:")
sp.pprint(J)

# testovaci bod
P2d = {x: 1, y: 2}

P3d = [expr.subs(P2d) for expr in F]
print(f"Vysledek v R^3: {P3d}")



# c) numerika a vizualizace
fig = plt.figure(figsize=(16, 8))

ax1 = fig.add_subplot(1, 2, 1)

x_1 = np.linspace(0.1, 1, 50)
y_1 = np.linspace(0.1, 1, 50)
X_1, Y_1 = np.meshgrid(x_1, y_1)

ax1.scatter(X_1, Y_1, c='blue', s=10, alpha=0.6)
ax1.set_title('Pred transformaci')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True, linestyle=':', alpha=0.6)

# aplikace transformace
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

U= X_1 + Y_1
V = X_1 * Y_1
W = X_1 ** Y_1

surf1 = ax2.plot_surface(U, V, W, cmap='plasma', edgecolor='none', alpha=0.8)
ax2.set_title('Po transformaci')
ax2.set_xlabel('u = x + y')
ax2.set_ylabel('v = x * y')
ax2.set_zlabel('w = x ^ y')


fig.colorbar(surf1, ax=ax2, shrink=0.4, aspect=10)
plt.suptitle ("Tranformace R^2 -> R^3")

# =========================================================

# 2) Obecne R3 -> R2
a = x + y * z
b = y + z * x

fun = sp.Matrix([a, b])
Xl = sp.Matrix([x, y, z])

# Jacobian
Jac = fun.jacobian(Xl)
print("Jacobiho matice zobrazení R^3 -> R^2:")
sp.pprint(Jac)

# testovaci bod
P3dim = {x: 2, y: 3, z: 4}
P2dim = [expr.subs(P3dim) for expr in fun]
print(f"Vysledek v R^2: {P2dim}\n")

# Vizualizace

xk = np.linspace(1, 2, 20)
yk = np.linspace(1, 2, 20)
zk = np.linspace(1, 2, 20)
Xk, Yk, Zk = np.meshgrid(xk, yk, zk)

A = Xk + Yk * Zk
B = Yk + Zk * Xk

# obrazek
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.scatter(Xk, Yk, Zk, c=Zk.ravel(), cmap='coolwarm', s=15, alpha=0.5)
ax1.set_title('Pred: 3D prostor (R^3)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax2 = fig.add_subplot(1, 2, 2)
scatter = ax2.scatter(A.ravel(), B.ravel(), c=Zk.ravel(), cmap='coolwarm', s=20, alpha=0.7)
ax2.set_title('Po transformaci (R^3 -> R^2)')
ax2.set_xlabel('u = x + y * z')
ax2.set_ylabel('v = y + z * x')
ax2.axhline(0, color='black', lw=0.8, linestyle='--')
ax2.axvline(0, color='black', lw=0.8, linestyle='--')
ax2.grid(True, linestyle=':', alpha=0.6)

fig.colorbar(scatter, ax=ax2, label='Původní hloubka Z')
plt.suptitle ("Tranformace R^3 -> R^2")


plt.tight_layout()
plt.show()