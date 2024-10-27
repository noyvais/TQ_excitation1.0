import numpy as np
import matplotlib.pyplot as plt

filename = input("Enter file name")
data_list = []
data = open(filename, "r+")
for line in data:
  line = line.replace("(", " ")
  line = line.replace(")", " ")
  line = line.replace(",", " ")
  raw_data = line.split()
  data_list.extend(raw_data)

data_list = [float(i) for i in data_list]
real_data = data_list[::2]
im_data = data_list[1::2]
real_data_arr = np.array(real_data)
im_data_arr = np.array(im_data)
matrix = np.reshape(real_data_arr, (8, 8))
heatmap = plt.imshow(np.absolute(matrix), cmap='YlOrBr')
for y in range(matrix.shape[0]):
    for x in range(matrix.shape[1]):
        plt.text(x, y, '%.4f' % matrix[y, x], horizontalalignment='center', verticalalignment='center')
plt.colorbar(heatmap)
plt.show()