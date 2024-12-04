import sys
import os

  # Z filter:
#data = open('3d-script_consecutive.py', 'r').readlines()
#data[41-1] = "T1line = 21\n"
#data[42-1] = "T2line = 22\n"
#data[43-1] = "TAUline = 23\n"
#data[50-1] = "  data = open('z-filter.in', 'r').readlines()\n"
#data[52-1] = "  fileq =  open('z-filter.in', 'w')\n"
#data[59-1] = "        os.system('simpson z-filter.in')\n"
#with open('3d-script_consecutive.py', 'w') as F:
#    F.writelines(data)
# replace TQC with ZF
#f = open('baseline.txt', "w")
#f.write("variable T3 , variable T4 , variable tau2 , lalalla")
#f.close()
#os.system("python 3d-script_consecutive.py 1.0 20.0 1.0 20.0 50.0 1.0 0.0 100.0 25.0")
# move PNGs to folder of zf results
#os.system("mv *.png ./zf_res")
"""
  # 2 pulses 
data = open('3d-script_consecutive.py', 'r').readlines()
data[41-1] = "T1line = 19\n"
data[42-1] = "T2line = 20\n"
data[43-1] = "TAUline = 18\n"
data[50-1] = "  data = open('2pls.in', 'r').readlines()\n"
data[52-1] = "  fileq =  open('2pls.in', 'w')\n"
data[59-1] = "        os.system('simpson 2pls.in')\n"
with open('3d-script_consecutive.py', 'w') as F:
    F.writelines(data)
os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 100.0 25.0")
## move PNGs to folder of zf results
os.system("mv *.png ./Cq=~10KHz/2pls/xy")
os.system("mv *.csv ./Cq=~10KHz/2pls/xy")


  # 4 pulses - 3 consecutive instead of first pulse:
data = open('3d-script_consecutive.py', 'r').readlines()
data[41-1] = "T1line = 19\n"
data[42-1] = "T2line = 20\n"
data[43-1] = "TAUline = 18\n"
data[50-1] = "  data = open('TQ_4pls1.in', 'r').readlines()\n"
data[52-1] = "  fileq =  open('TQ_4pls1.in', 'w')\n"
data[59-1] = "        os.system('simpson TQ_4pls1.in')\n"
with open('3d-script_consecutive.py', 'w') as F:
    F.writelines(data)
os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 100.0 25.0")
# move PNGs to folder of zf results
os.system("mv *.png ./Cq=~750KHz/4pls1/yxyx")
os.system("mv *.csv ./Cq=~750KHz/4pls1/yxyx")

  # 4 pulses - 3 consecutive instead of second pulse:
data = open('3d-script_consecutive.py', 'r').readlines()
data[41-1] = "T1line = 19\n"
data[42-1] = "T2line = 20\n"
data[43-1] = "TAUline = 18\n"
data[50-1] = "  data = open('TQ_4pls2.in', 'r').readlines()\n"
data[52-1] = "  fileq =  open('TQ_4pls2.in', 'w')\n"
data[59-1] = "        os.system('simpson TQ_4pls2.in')\n"
with open('3d-script_consecutive.py', 'w') as F:
    F.writelines(data)
os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 100.0 25.0")
## move PNGs to folder of zf results
os.system("mv *.png ./Cq=~750KHz/4pls2/yxyx")
os.system("mv *.csv ./Cq=~750KHz/4pls2/yxyx")

  # 3 pulses - 2 consecutive instead of first pulse:
data = open('3d-script_consecutive.py', 'r').readlines()
data[41-1] = "T1line = 19\n"
data[42-1] = "T2line = 20\n"
data[43-1] = "TAUline = 18\n"
data[50-1] = "  data = open('TQ_3pulse.in', 'r').readlines()\n"
data[52-1] = "  fileq =  open('TQ_3pulse.in', 'w')\n"
data[59-1] = "        os.system('simpson TQ_3pulse.in')\n"
with open('3d-script_consecutive.py', 'w') as F:
    F.writelines(data)
os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 100.0 25.0")
# move PNGs to folder of zf results
os.system("mv *.png ./Cq=~750KHz/3pls1/yxy")
os.system("mv *.csv ./Cq=~750KHz/3pls1/yxy")

  # 3 pulses - 2 consecutive instead of second pulse:
data = open('3d-script_consecutive.py', 'r').readlines()
data[41-1] = "T1line = 19\n"
data[42-1] = "T2line = 20\n"
data[43-1] = "TAUline = 18\n"
data[50-1] = "  data = open('TQ_3pulse2.in', 'r').readlines()\n"
data[52-1] = "  fileq =  open('TQ_3pulse2.in', 'w')\n"
data[59-1] = "        os.system('simpson TQ_3pulse2.in')\n"
with open('3d-script_consecutive.py', 'w') as F:
    F.writelines(data)
os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 100.0 25.0")
# move PNGs to folder of zf results
os.system("mv *.png ./Cq=~750KHz/3pls2/yxy")
os.system("mv *.csv ./Cq=~750KHz/3pls2/yxy")
"""
phases = []

for i in range(4):
  if i==0:
    data = open('singlepls.in', 'r').readlines()
    data[26-1] = "    pulse $T1 $par(rf) x\n"
    with open('singlepls.in', 'w') as F:
      F.writelines(data)
      
    data = open('2pls.in', 'r').readlines()
    data[31-1] =  "    pulse $T1 $par(rf) x\n"
    data[33-1] =  "    pulse $T2 $par(rf) x\n"
    with open('2pls.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[34-1] =  "    pulse $T1 $par(rf) y\n"
    data[36-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_3pulse.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) x\n"
    data[41-1] =  "    pulse $T2 $par(rf) y\n"
    data[42-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_3pulse2.in', 'w') as F:
      F.writelines(data)
      
      data = open('TQ_4pls1.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[34-1] =  "    pulse $T1 $par(rf) y\n"
    data[35-1] =  "    pulse $T1 $par(rf) x\n"
    data[37-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls1.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_4pls2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) x\n"
    data[41-1] =  "    pulse $T2 $par(rf) y\n"
    data[42-1] =  "    pulse $T2 $par(rf) x\n"
    data[43-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls2.in', 'w') as F:
      F.writelines(data)
      
    phases=["x", "xx", "xyx", "xyx", "xyxy", "xyxy"]
      
  elif i==1:
    data = open('2pls.in', 'r').readlines()
    data[31-1] =  "    pulse $T1 $par(rf) x\n"
    data[33-1] =  "    pulse $T2 $par(rf) y\n"
    with open('2pls.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[34-1] =  "    pulse $T1 $par(rf) x\n"
    data[36-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_3pulse.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) y\n"
    data[41-1] =  "    pulse $T2 $par(rf) x\n"
    data[42-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_3pulse2.in', 'w') as F:
      F.writelines(data)
      
      data = open('TQ_4pls1.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[34-1] =  "    pulse $T1 $par(rf) x\n"
    data[35-1] =  "    pulse $T1 $par(rf) y\n"
    data[37-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls1.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_4pls2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) y\n"
    data[41-1] =  "    pulse $T2 $par(rf) x\n"
    data[42-1] =  "    pulse $T2 $par(rf) y\n"
    data[43-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls2.in', 'w') as F:
      F.writelines(data)
    
    phases=["x", "xy", "yxy", "yxy", "yxyx", "yxyx"]
      
  elif i==2:
    data = open('2pls.in', 'r').readlines()
    data[31-1] =  "    pulse $T1 $par(rf) y\n"
    data[33-1] =  "    pulse $T2 $par(rf) x\n"
    with open('2pls.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[34-1] =  "    pulse $T1 $par(rf) x\n"
    data[36-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_3pulse.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) x\n"
    data[41-1] =  "    pulse $T2 $par(rf) x\n"
    data[42-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_3pulse2.in', 'w') as F:
      F.writelines(data)
      
      data = open('TQ_4pls1.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[34-1] =  "    pulse $T1 $par(rf) x\n"
    data[35-1] =  "    pulse $T1 $par(rf) y\n"
    data[37-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls1.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_4pls2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) x\n"
    data[41-1] =  "    pulse $T2 $par(rf) x\n"
    data[42-1] =  "    pulse $T2 $par(rf) y\n"
    data[43-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls2.in', 'w') as F:
      F.writelines(data)
      
    phases=["x", "yx", "yxx", "xxy", "yxyy", "xxyx"]
      
  elif i==3:
    data = open('2pls.in', 'r').readlines()
    data[31-1] =  "    pulse $T1 $par(rf) y\n"
    data[33-1] =  "    pulse $T2 $par(rf) y\n"
    with open('2pls.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[34-1] =  "    pulse $T1 $par(rf) y\n"
    data[36-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_3pulse.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_3pulse2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) y\n"
    data[41-1] =  "    pulse $T2 $par(rf) y\n"
    data[42-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_3pulse2.in', 'w') as F:
      F.writelines(data)
      
      data = open('TQ_4pls1.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[34-1] =  "    pulse $T1 $par(rf) y\n"
    data[35-1] =  "    pulse $T1 $par(rf) x\n"
    data[37-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls1.in', 'w') as F:
      F.writelines(data)
      
    data = open('TQ_4pls2.in', 'r').readlines()
    data[39-1] =  "    pulse $T1 $par(rf) y\n"
    data[41-1] =  "    pulse $T2 $par(rf) y\n"
    data[42-1] =  "    pulse $T2 $par(rf) x\n"
    data[43-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls2.in', 'w') as F:
      F.writelines(data)
    
    phases=["x", "yy", "xyy", "yyx", "xyxx", "yyxy"]

  Cq = [60, 150, 300, 450]
  for c in Cq:
    """
    data = open('singlepls.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('singlepls.in', 'w') as F:
      F.writelines(data)
      
    data = open('1d-script.py', 'r').readlines()
    data[25-1] = "T1line = 18\n"
    data[30-1] = "  data = open('singlepls.in', 'r').readlines()\n"
    data[32-1] = "  fileq =  open('singlepls.in', 'w')\n"
    data[37-1] = "      os.system('simpson singlepls.in')\n"
    with open('1d-script.py', 'w') as F:
        F.writelines(data)
    f = open('1pls-baseline.txt', "w")
    f.write("variable T1 , ")
    f.close()
    os.system("python 1d-script.py  1.0 50.0 1.0")
    # move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/1pls/x")
    os.system(f"mv *.csv ./Cq=~{c}KHz/1pls/x")  
    """
    data = open('2pls.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('2pls.in', 'w') as F:
      F.writelines(data) 
    
      # 2 pulses 
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('2pls.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('2pls.in', 'w')\n"
    data[59-1] = "        os.system('simpson 2pls.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
    ## move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/2pls/{phases[1]}")
    os.system(f"mv *.csv ./Cq=~{c}KHz/2pls/{phases[1]}")
    
    data = open('TQ_4pls1.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('TQ_4pls1.in', 'w') as F:
      F.writelines(data) 
    
      # 4 pulses - 3 consecutive instead of first pulse:
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('TQ_4pls1.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('TQ_4pls1.in', 'w')\n"
    data[59-1] = "        os.system('simpson TQ_4pls1.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
    # move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/4pls1/{phases[4]}")
    os.system(f"mv *.csv ./Cq=~{c}KHz/4pls1/{phases[4]}")
    
    data = open('TQ_4pls2.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('TQ_4pls2.in', 'w') as F:
      F.writelines(data) 
  
    # 4 pulses - 3 consecutive instead of second pulse:
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('TQ_4pls2.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('TQ_4pls2.in', 'w')\n"
    data[59-1] = "        os.system('simpson TQ_4pls2.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
    ## move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/4pls2/{phases[5]}")
    os.system(f"mv *.csv ./Cq=~{c}KHz/4pls2/{phases[5]}")
    
    data = open('TQ_3pulse.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('TQ_3pulse.in', 'w') as F:
      F.writelines(data) 
  
    # 3 pulses - 2 consecutive instead of first pulse:
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('TQ_3pulse.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('TQ_3pulse.in', 'w')\n"
    data[59-1] = "        os.system('simpson TQ_3pulse.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
  # move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/3pls1/{phases[2]}")
    os.system(f"mv *.csv ./Cq=~{c}KHz/3pls1/{phases[2]}")
    
    data = open('TQ_3pulse2.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('TQ_3pulse2.in', 'w') as F:
      F.writelines(data) 
  
    # 3 pulses - 2 consecutive instead of second pulse:
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('TQ_3pulse2.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('TQ_3pulse2.in', 'w')\n"
    data[59-1] = "        os.system('simpson TQ_3pulse2.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
    # move PNGs to folder of zf results
    os.system(f"mv *.png ./Cq=~{c}KHz/3pls2/{phases[3]}")
    os.system(f"mv *.csv ./Cq=~{c}KHz/3pls2/{phases[3]}")

  
    