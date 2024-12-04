import imageio.v2 as imageio
import os
from pathlib import Path

#images = Path('./').glob('*.png')
images = [f for f in os.listdir('./') if f.endswith('.png')]
# sort by name
images = sorted(images)
print(images)
files=[]
for img in images:
  files.append(img)
  
ims = [imageio.imread(f) for f in files]
imageio.mimwrite('final.gif', ims, format='gif', duration=1200)