import sys
import os
import subprocess
import shutil
from shutil import copyfileobj
from io import DEFAULT_BUFFER_SIZE

with open(sys.argv[1]+'.txt', 'rb') as input1, open(sys.argv[2]+'.txt', 'rb') as input2, open('output.bin', 'wb') as output:
    copyfileobj(input1, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input2, output, DEFAULT_BUFFER_SIZE)
    input1.close
    input2.close
    output.close
os.remove(sys.argv[1]+'.txt')
os.remove(sys.argv[2]+'.txt')