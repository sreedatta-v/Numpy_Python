import numpy as np
from numpy import shape

# if you start with this array:
a = np.array([1,2,3,5,6,7])
print(shape(a))

# You can use np.newaxis to add a new axis:
a2 = a[np.newaxis, :]
print(shape(a2))

# Output : (6,) for shape(a)
# (1, 6) for shape(a2)

""" You can also expand an array by inserting a new axis at a specified position with np.expand_dims """

b = np.expand_dims(a, axis=1)
print(shape(b))

#Output : (6,1)