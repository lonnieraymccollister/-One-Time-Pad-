import sys
import os
import subprocess
import shutil
from shutil import copyfileobj
from io import DEFAULT_BUFFER_SIZE

with open(sys.argv[1]+'.txt', 'rb') as input1, open(sys.argv[2]+'.txt', 'rb') as input2, sys.argv[3]+'.txt', 'rb') as input3, open(sys.argv[4]+'.txt', 'rb') as input4, open('output.bin', 'wb') as output:
    copyfileobj(input1, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input2, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input3, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input4, output, DEFAULT_BUFFER_SIZE)
    input1.close
    input2.close
    input3.close
    input4.close
    output.close
os.remove(sys.argv[1]+'.txt')
os.remove(sys.argv[2]+'.txt')
os.remove(sys.argv[3]+'.txt')
os.remove(sys.argv[4]+'.txt')
