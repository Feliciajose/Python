#8-d) SCIPY
# Scipy - solving linear equations
#importing the scipy and numpy packages
fromscipy import linalg
importnumpy as np
#Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
#Passing the values to the solve function
x = linalg.solve(a, b)
#printing the result array
print(x)
"""
Given input
3x + 2y = 2
x - y = 4
5y + z = -1
"""