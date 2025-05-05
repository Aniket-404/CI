import numpy as np
import matplotlib.pyplot as plt

def triangular_mf(x, a, b, c):
    """
    Triangular membership function.
    
    Parameters:
    - x: input value or array
    - a: left point
    - b: peak point
    - c: right point
    
    Returns:
    - Membership value(s)
    """
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# Input range
x_vals = np.linspace(0, 10, 100)

# Triangular MF parameters (a=2, b=5, c=8)
mf_vals = triangular_mf(x_vals, 2, 5, 8)

# Plotting
plt.plot(x_vals, mf_vals, label='Triangular MF (a=2, b=5, c=8)', color='blue')
plt.title("Triangular Membership Function")
plt.xlabel("x")
plt.ylabel("Membership Degree")
plt.grid(True)
plt.legend()
plt.show()
