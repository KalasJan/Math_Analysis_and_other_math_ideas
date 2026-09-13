# Make (and plot) the Recaman's sequence:
# a0 = 0
# a_n = a_(n-1) - n / if a_(n-1) - n > 0 or unvisited
# a_n = a_(n-1) + n / otherwise

import numpy as np
import matplotlib.pyplot as plt

def Recaman(terms):
    sequence = [0]
    visited = {0}
    
    for n in range (1, terms):
        prev = sequence[-1]
        candidate = prev - n
        
        # a_n = a_(n-1) - n if > 0 and unvisited, otherwise + n
        if candidate > 0 and candidate not in visited:
            next_val = candidate
        else: next_val = prev + n
        
        sequence.append(next_val)
        visited.add(next_val)
    
    return sequence

# generate sequence
terms = 100
seq = Recaman(terms)
n_indices = np.arange(terms)

print (seq)

# Graph
fig, ax = plt.subplots(figsize = (12,6))

# half circles
for i in range (len(seq) - 1):
    start = seq[i]
    end = seq[i+1]
    
    center = (start + end) / 2
    rad = abs(end - start) / 2
    
# angles
    angle = np.linspace(0, np.pi, 100)

    if i % 2 == 0:
        y_sign = 1 # above axis
    else:
        y_sign = -1 # under axis
        
    x_arc = center + rad * np.cos(angle)
    y_arc = rad * np.sin(angle) * y_sign  # positive or negative
    
    ax.plot(x_arc, y_arc, color = 'crimson', alpha=0.7, linewidth=1)
    
# Special points
ax.scatter(seq, np.zeros_like(seq), color='black', s=15, zorder=5)

# Titles
ax.set_title("Recaman's Sequence - Semicircular Visualization", fontsize=14)
ax.set_xlabel('Hodnota $a_n$', fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.set_aspect('equal') 
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()
