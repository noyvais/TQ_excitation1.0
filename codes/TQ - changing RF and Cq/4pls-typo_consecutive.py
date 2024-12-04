import sys
import os

phases = ["yyxx", "yxyy", "xyxx", "xxyy"]  
for i in range(4):
  if i==0:
    data = open('TQ_4pls-typo.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[35-1] =  "    pulse $T2 $par(rf) x\n"
    data[36-1] =  "    pulse $T2 $par(rf) y\n"
    data[37-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls-typo.in', 'w') as F:
      F.writelines(data)  
  if i==1:
    data = open('TQ_4pls-typo.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[35-1] =  "    pulse $T2 $par(rf) x\n"
    data[36-1] =  "    pulse $T2 $par(rf) y\n"
    data[37-1] =  "    pulse $T2 $par(rf) y\n"
    with open('TQ_4pls-typo.in', 'w') as F:
      F.writelines(data)  
  if i==2:
    data = open('TQ_4pls-typo.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) x\n"
    data[35-1] =  "    pulse $T2 $par(rf) y\n"
    data[36-1] =  "    pulse $T2 $par(rf) x\n"
    data[37-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls-typo.in', 'w') as F:
      F.writelines(data)  
  if i==3:
    data = open('TQ_4pls-typo.in', 'r').readlines()
    data[33-1] =  "    pulse $T1 $par(rf) y\n"
    data[35-1] =  "    pulse $T2 $par(rf) y\n"
    data[36-1] =  "    pulse $T2 $par(rf) x\n"
    data[37-1] =  "    pulse $T2 $par(rf) x\n"
    with open('TQ_4pls-typo.in', 'w') as F:
      F.writelines(data)  

      
  Cq = [50, 5, 15, 20, 25, 30, 60]
  for c in Cq:
    data = open('TQ_4pls-typo.in', 'r').readlines()
    data[4-1] = f"    quadrupole 1 1 {c*1000} 0.6 0 0 0\n"
    with open('TQ_4pls-typo.in', 'w') as F:
      F.writelines(data) 
    
    data = open('3d-script_consecutive.py', 'r').readlines()
    data[41-1] = "T1line = 19\n"
    data[42-1] = "T2line = 20\n"
    data[43-1] = "TAUline = 18\n"
    data[50-1] = "  data = open('TQ_4pls-typo.in', 'r').readlines()\n"
    data[52-1] = "  fileq =  open('TQ_4pls-typo.in', 'w')\n"
    data[59-1] = "        os.system('simpson TQ_4pls-typo.in')\n"
    with open('3d-script_consecutive.py', 'w') as F:
      F.writelines(data)
    os.system("python 3d-script_consecutive.py  1.0 50.0 1.0 1.0 50.0 1.0 0.0 75.0 25.0")
    ## move PNGs to folder of zf results
    os.system(f"mkdir --parents ./Cq=~{c}KHz/4pls-typo-new/{phases[i]}; mv *.png *.csv ./Cq=~{c}KHz/4pls-typo-new/{phases[i]}")