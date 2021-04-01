#!/usr/bin/env python3

import sys
import os
import numpy as np
from PIL import Image


# Define width and height
w, h = 800, 800

# Read file using numpy "fromfile()"
with open(sys.argv[1], mode='rb') as f:
    d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape(h,w)

# Make into PIL Image and save
PILimage = Image.fromarray(d)
PILimage.save('TestImg.png')