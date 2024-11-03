import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(y.size)
z = np.concatenate((x, y), axis=0)
print(z)
n = np.array([[[1], [2]], [[3], [4]]])
print(n)
print(n.shape)
