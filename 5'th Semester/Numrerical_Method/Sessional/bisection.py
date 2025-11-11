import matplotlib.pyplot as plt
import numpy as np

def bisection(a, b):
    while b - a > 0.0001:
        c = (a + b) / 2
        if (f(a) * f(c)) < 0:
            b = c
        else:
            a = c
    return c

f = lambda x: x**3 - x - 2

a = float(input("enter initial guess a: "))
b = float(input("enter initial guess b: "))

root = bisection(a, b)
print("Root =", root)

x = np.linspace(a - 1, b + 1, 400)
y = f(x)

plt.plot(x, y, label='f(x) = x³ - x - 2')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(root, color='red', linestyle='--', label=f'Root = {root:.5f}')
plt.scatter(root, f(root), color='red')
plt.title('Bisection Method Visualization')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(1)
plt.show()
