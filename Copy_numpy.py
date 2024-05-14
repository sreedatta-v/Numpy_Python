import numpy as np

a = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(a)

a[0] = 99
print(a)

b = a.copy()
print("Array b: ",b)
