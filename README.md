# NumPy_Python
## Introduction to NumPy 
NumPy (**Numerical Python**) is an open source Python library that’s used in almost every field of science and engineering. It’s the universal standard for working with numerical data in Python, and it’s at the core of the scientific Python and PyData ecosystems

The NumPy library contains multidimensional array and matrix data structures.

It provides **`ndarray**,` <i>a homogeneous n-dimensional array object,</i> with methods to efficiently operate on it. NumPy can be used to perform a wide variety of mathematical operations on arrays.

## Installing NumPy

To install NumPy
`pip install numpy` 

### **How to import NumPy**

`import numpy as np`

We shorten the imported name to `np` for better readability of code using NumPy.

## What is an array? 
n array is a central data structure of the NumPy library.

An array can be indexed by a tuple of nonnegative integers, by booleans, by another array, or by integers. The `rank` of the array is the number of dimensions. The `shape` of the array is a tuple of integers giving the size of the array along each dimension.

`a = np.array([1, 2, 3, 4, 5, 6])`

*#As we need to access the elements within the array we use the Square Bracket.*

## ndarray
An N-dimensional array is simply an array with any number of dimensions

The NumPy `ndarray` class is used to represent both matrices and vectors.

> A **vector** is an array with a single dimension (there’s no difference between row and column vectors), while a **matrix** refers to an array with two dimensions. For **3-D** or higher dimensional arrays, the term **tensor** is also commonly used.
> 

### **What are the attributes of an array?**

An array is usually a fixed-size container of items of the same type and size. 

The number of dimensions and items in an array is defined by its shape. The shape of an array is a tuple of non-negative integers that specify the sizes of each dimension.

In NumPy, dimensions are called axes.

### Basic Operations using NumPy
1. np.array(),
2. np.zeros(),
3. np.ones(),
4. np.empty(),
5. np.arange(),
6. np.linspace(),
7. dtype
