import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
#import logging
#logging.basicConfig(level=logging.DEBUG)
#numpy.set_printoptions(threshold=numpy.inf)

CQline = 5
Qline = 19
CQ_index = -1
CQ_baseline = "quadrupole 1 2 "
CQ_baseline2 = " 0.12 20 60 18"
Q_baseline = "variable q "

CQ= numpy.array([5, 50, 500])

def replacement(lineNum, content):
  data = open('static_base.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('static_base.in', 'w')
  fileq.writelines(data)
  datam = open('mas_base.in', 'r').readlines()
  datam[lineNum-1] = '{}\n'.format(content)
  fileqm =  open('mas_base.in', 'w')
  fileqm.writelines(datam)
  
for i in range(len(CQ)):
  CQ_index = CQ_index+1
  replacement(CQline, CQ_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]*1000) + CQ_baseline2)
  replacement(Qline, Q_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]))
  #os.system("simpson static_base.in")
  #os.system("simpson mas_base.in")
  x = numpy.loadtxt('static_base'+str(CQ[i])+'.spe', usecols=(0), skiprows=512, max_rows=1024)
  y = numpy.loadtxt('static_base'+str(CQ[i])+'.spe', usecols=(1), skiprows=512, max_rows=1024)
  xm = numpy.loadtxt('mas_base'+str(CQ[i])+'.spe', usecols=(0), skiprows=512, max_rows=1024)
  ym = numpy.loadtxt('mas_base'+str(CQ[i])+'.spe', usecols=(1), skiprows=512, max_rows=1024)
  plt.plot(xm, ym, label="MAS")
  plt.plot(x, y, label="static")
  plt.title("Lineshape of MAS vs Static, CQ="+str(CQ[i])+"kHz")
  ax = plt.gca()
  ax.get_yaxis().set_visible(False)
  ax.set_ylim(-100,1600)
  plt.xlabel("Chemical Shift [Hz]")
  print('hi')
  plt.legend(loc="upper left")
  print('hi')
  plt.savefig("static"+str(CQ[i])+".png", dpi=300)
  plt.show()