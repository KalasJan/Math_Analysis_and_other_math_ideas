# Plotting Mobius strip and Klein bottle

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # colors

# =========================================================

# 1) Mobius strip

# parametres
um = np.linspace(0, 2* np.pi, 100) # length
vm = np.linspace(-0.2, 0.2, 50) # width
Um, Vm = np.meshgrid(um, vm)

Rm = 2 # radius

# parametric equation (U/2 - rotation of the end of the strip)
Xm = (Rm + Vm * np.cos(Um / 2)) * np.cos(Um)
Ym = (Rm + Vm * np.cos(Um / 2)) * np.sin(Um)
Zm = Vm * np.sin(Um / 2)

# plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# colors
ax.plot_surface(Xm, Ym, Zm, rstride=5, cstride=5, cmap=cm.viridis,
                edgecolor='none', alpha=0.9, antialiased=True)

# axis and details
ax.set_title("Möbius strip / Möbiův list")
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

ax.set_box_aspect([1, 1, 0.5])
ax.grid(False)
ax.set_axis_off()

plt.show()

# ==================================================================

# 2) Kleins bottle

# parametres
uk = np.linspace(0, 2 * np.pi, 100)
vk = np.linspace(0, 2 * np.pi, 100)
Uk, Vk = np.meshgrid(uk, vk)

# "8 shape"
rk = 4 * (1 - np.cos(Uk) / 2) # shape

# equation
# up and down part
Xk = np.where(Uk < np.pi,
             6 * np.cos(Uk) * (1 + np.sin(Uk)) + rk * np.cos(Uk) * np.cos(Vk),
             6 * np.cos(Uk) * (1 + np.sin(Uk)) - rk * np.cos(Vk))
Yk = np.where(Uk < np.pi,
             16 * np.sin(Uk) + rk * np.sin(Uk) * np.cos(Vk),
             16 * np.sin(Uk))

# part going to the bottle
Zk = np.where(Uk < np.pi,
             rk * np.sin(Vk),
             -rk * np.cos(Vk))

# plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# necessary to see the self-intersection
gra = ax.plot_surface(Xk, Yk, Zk, rstride=2, cstride=2, cmap=cm.magma,
                linewidth=0.1, antialiased=True, alpha=0.7)

# axis
ax.set_title("Klein bottle / Kleinova lahev")
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

ax.set_box_aspect([1, 1, 2])
ax.grid(False)
ax.set_axis_off()

plt.show()

# ===============================================================

# 3) Both in 1 pic

fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(121, projection='3d') # mobius
ax2 = fig.add_subplot(122, projection='3d') # klein

ax1.plot_surface(Xm, Ym, Zm, rstride=5, cstride=5, cmap=cm.viridis,
                edgecolor='none', alpha=0.9, antialiased=True)
ax1.set_title("Möbius strip / Möbiův list")
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_zlabel('Z')

ax1.set_box_aspect([1, 1, 1.5])
ax1.grid(False)
ax1.set_axis_off()

ax2.plot_surface(Xk, Yk, Zk, rstride=2, cstride=2, cmap=cm.magma,
                linewidth=0.1, antialiased=True, alpha=0.7)
ax2.set_title("Klein bottle / Kleinova lahev")
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_zlabel('Z')

ax2.set_box_aspect([1, 1, 1.5])
ax2.grid(False)
ax2.set_axis_off()

plt.suptitle("Topological objects / Topologické objekty", fontsize=14)
plt.tight_layout()
plt.show()