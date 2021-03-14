import sys
import os
import subprocess
import shutil
from shutil import copyfileobj
from io import DEFAULT_BUFFER_SIZE

with open(sys.argv[1]+'.txt', 'rb') as input1, open(sys.argv[2]+'.txt', 'rb') as input2, sys.argv[3]+'.txt', 'rb') as input3, open(sys.argv[4]+'.txt', 'rb') as input4, sys.argv[5]+'.txt', 'rb') as input5, open(sys.argv[6]+'.txt', 'rb') as input6, sys.argv[7]+'.txt', 'rb') as input7, open(sys.argv[8]+'.txt', 'rb') as input8, sys.argv[9]+'.txt', 'rb') as input9, open(sys.argv[10]+'.txt', 'rb') as input10, sys.argv[11]+'.txt', 'rb') as input11, open(sys.argv[12]+'.txt', 'rb') as input12, sys.argv[13]+'.txt', 'rb') as input13, open(sys.argv[14]+'.txt', 'rb') as input14, sys.argv[15]+'.txt', 'rb') as input15, open(sys.argv[16]+'.txt', 'rb') as input16, open('output.bin', 'wb') as output:
    copyfileobj(input1, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input2, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input3, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input4, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input5, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input6, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input7, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input8, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input9, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input10, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input11, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input12, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input13, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input14, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input15, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input16, output, DEFAULT_BUFFER_SIZE)
    input1.close
    input2.close
    input3.close
    input4.close
    input5.close
    input6.close
    input7.close
    input8.close
    input9.close
    input10.close
    input11.close
    input12.close
    input13.close
    input14.close
    input15.close
    input16.close
    output.close
os.remove(sys.argv[1]+'.txt')
os.remove(sys.argv[2]+'.txt')
os.remove(sys.argv[3]+'.txt')
os.remove(sys.argv[4]+'.txt')
os.remove(sys.argv[5]+'.txt')
os.remove(sys.argv[6]+'.txt')
os.remove(sys.argv[7]+'.txt')
os.remove(sys.argv[8]+'.txt')
os.remove(sys.argv[9]+'.txt')
os.remove(sys.argv[10]+'.txt')
os.remove(sys.argv[11]+'.txt')
os.remove(sys.argv[12]+'.txt')
os.remove(sys.argv[13]+'.txt')
os.remove(sys.argv[14]+'.txt')
os.remove(sys.argv[15]+'.txt')
os.remove(sys.argv[16]+'.txt')