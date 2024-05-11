"""
NumPy (**Numerical Python**) is an `open source Python library` that’s used in almost every field of science and engineering. It’s the universal standard for `working with numerical data in Python,` and it’s at the core of the scientific Python and PyData ecosystems

The NumPy library contains `multidimensional array and matrix data structures.`

It provides `ndarray,` a homogeneous n-dimensional array object, with methods to efficiently operate on it. NumPy can be used to perform a `wide variety of mathematical operations on arrays.`
"""
import numpy as np

# Creation of np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(), dtype

# to create a NumPy array, we can use the function np.array().
a = np.array([1, 2, 3, 4, 5, 6])
print(a[4])

# array filled with 0’s:
b = np.zeros(2)
print(b)

# Or an array filled with 1’s:
c = np.ones(5)
print(c)

# or an empty array - returns random value for initial index.
d = np.empty(3)
print(d)

# or array with a range of elements
e = np.arange(5)
print(e)

# an array that contains a range of evenly spaced intervals. To do this, you will specify the
# first number, last number, and the step size.
e1 = np.arange(1,15,2)
print(e1)

# use np.linspace() to create an array with values that are spaced linearly in a specified interval:
f = np.linspace(0, 10, num=5)
print(f)

# While the default data type is floating point (np.float64), you can explicitly specify which data type you want using the dtype keyword.
g = x = np.ones(2, dtype=np.int64)
print(g)

