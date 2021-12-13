import numpy as np

data = np.genfromtxt('dataset.csv',dtype=int,delimiter='\t')
data = data[1:,:]
print(data)

print(data.shape)
print(data.dtype)