import os
import numpy
import math
import cmath
from scipy import signal
from scipy import fftpack
import scipy.io
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)

fileName="ser"
endianess='"l"'

nd = 10240
nd_acq_file=10240
diff = nd-nd_acq_file
ni=19

# get bruker format to a normal format - for now. later, it will be binary to begin with
os.system("od -An -i -v -w4 {} > {}.txt".format(fileName, fileName))
os.system("perl -pe '$_=pack{}, $_' < {}.txt > {}_binary_dump".format(endianess, fileName, fileName))
with open("{}_binary_dump".format(fileName), "rb") as f:
  data = numpy.fromfile(f, numpy.int32)
f.close()

# check if needed ????
im_data = data[1::2]  
real_data = data[::2]  

real_interferogram = numpy.reshape(real_data, (ni, int(nd/2)))
im_interferogram = numpy.reshape(im_data, (ni, int(nd/2)))

with open("{}_final_bin_real".format(fileName), "wb") as f2:
  real_data = numpy.save(f2, real_interferogram)
f2.close()

with open("{}_final_bin_im".format(fileName), "wb") as f3:
  im_data = numpy.save(f3, im_interferogram)
f3.close()

with open("{}_final_bin_real".format(fileName), "rb") as f:
  real_time_domain = numpy.load(f)
f.close()

with open("{}_final_bin_im".format(fileName), "rb") as f1:
  imag_time_domain = numpy.load(f1)
f1.close()

time_domain_mat_real = numpy.reshape(real_time_domain, (ni, int(nd/2)))
time_domain_mat_imag = numpy.reshape(imag_time_domain, (ni, int(nd/2)))

for i in range(int(diff/2)):
  time_domain_mat_real = numpy.delete(time_domain_mat_real, 0, 1)
  time_domain_mat_imag = numpy.delete(time_domain_mat_imag, 0, 1)

nd = time_domain_mat_imag.shape[1]
print(nd)
print(ni)

time_domain_mat = numpy.empty((ni, nd), dtype=numpy.complex128)
time_domain_mat.real = time_domain_mat_real
time_domain_mat.imag = time_domain_mat_imag

#time_domain_mat = numpy.reshape(data, (ni, nd))
file_path = '2d-popt.mat'
scipy.io.savemat(file_path, {'data': time_domain_mat})