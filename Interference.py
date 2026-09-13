# Interference of waves from N sources
# u(x,y,t) = sum_{i = 1} ^N 1/sqrt(1+alfa * r_i) * cos(k*r_i - omega * t)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 10.0      # wave number
omega = 5.0   # angular frequency
alfa = 0.1    # attenuation factor
t = 3.0       # time

# Coordinates grid
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Define sources positions [(x_1, y_1), (x_2, y_2), ...]
sources = [ # max N points
    (-2.0, 0.0),
    (2.0, 0.0),
    (0.0, 3.0),
]

# Calculate interference field u(x, y, t)
U = np.zeros_like(X)

for sx, sy in sources:
    # distance r_i from source (sx, sy) to each point (X, Y)
    r_i = np.sqrt((X - sx)**2 + (Y - sy)**2)
    
    # Avoid division by zero if a point hits the exact source location
    r_i = np.clip(r_i, 1e-5, None)
    
    # Wave contribution from this source
    amplitude = 1.0 / np.sqrt(1.0 + alfa * r_i)
    phase = k * r_i - omega * t
    
    U += amplitude * np.cos(phase)

# Plotting the interference pattern
fig, ax = plt.subplots(figsize=(8, 7))

# Use 'coolwarm', 'viridis' or 'inferno' colormap for wave peaks and troughs
im = ax.imshow(U, extent=[-5, 5, -5, 5], origin='lower', cmap='inferno_r', alpha=0.9)

# Mark sources positions
for i, (sx, sy) in enumerate(sources):
    lbl = 'Sources' if i == 0 else None
    ax.scatter(sx, sy, color='lightgreen', s=50, marker='o', zorder=5, label=lbl)

ax.set_title(f"Wave Interference ({len(sources)} sources) | t = {t} s", fontsize=14)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
fig.colorbar(im, ax=ax, label='$u(x,y,t)$')

plt.tight_layout()
plt.show()