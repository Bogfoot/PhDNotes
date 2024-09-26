import numpy as np
import matplotlib.pyplot as plt

# Create theta values from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 500)

# Calculate the real and imaginary parts of e^(i*theta)
x = np.cos(theta)
y = np.sin(theta)

# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y, label=r'$e^{i\theta}$')

# Add labels to the specific points
plt.text(1, 0, r'$\phi_+$', fontsize=12, ha='left', va='center')
plt.text(0, 1, r'$\phi_+^i$', fontsize=12, ha='center', va='bottom')
plt.text(-1, 0, r'$\phi_-$', fontsize=12, ha='right', va='center')
plt.text(0, -1, r'$\phi_-^i$', fontsize=12, ha='center', va='top')

# Set axis limits and labels
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Label the axes
plt.xlabel('Re')
plt.ylabel('Im')

# Equal aspect ratio
plt.gca().set_aspect('equal')

# Show the plot
plt.title(r'Plot of $e^{i \theta}$ with labeled points')
plt.grid(True)
plt.show()
