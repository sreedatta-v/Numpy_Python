import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a[2:6])

a1 = np.array([[1, 2],
               [3, 4]])

a2 = np.array([[5, 6],
               [7, 8]])

print(a1 + a2)
b = np.vstack((a1, a2))
print(b)

c = np.hstack((a1,a2))
print(c)

d = np.hsplit(a1,a2)
print(d)