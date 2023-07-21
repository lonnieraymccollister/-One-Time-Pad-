import sys
import os
import subprocess
import shutil
from shutil import copyfileobj
from io import DEFAULT_BUFFER_SIZE

with open(sys.argv[1]+'.txt', 'rb') as input1, open(sys.argv[2]+'.txt', 'rb') as input2, open(sys.argv[3]+'.txt', 'rb') as input3, open(sys.argv[4]+'.txt', 'rb') as input4, open(sys.argv[5]+'.txt', 'rb') as input5, open(sys.argv[6]+'.txt', 'rb') as input6, open(sys.argv[7]+'.txt', 'rb') as input7, open(sys.argv[8]+'.txt', 'rb') as input8, open(sys.argv[1]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]+'_'+sys.argv[5]+'_'+sys.argv[6]+'_'+sys.argv[7]+'_'+sys.argv[8]+'.txt', 'wb') as output:
    copyfileobj(input1, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input2, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input3, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input4, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input5, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input6, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input7, output, DEFAULT_BUFFER_SIZE)
    copyfileobj(input8, output, DEFAULT_BUFFER_SIZE)
    input1.close
    input2.close
    input3.close
    input4.close
    input5.close
    input6.close
    input7.close
    input8.close
    output.close
os.remove(sys.argv[1]+'.txt')
os.remove(sys.argv[2]+'.txt')
os.remove(sys.argv[3]+'.txt')
os.remove(sys.argv[4]+'.txt')
os.remove(sys.argv[5]+'.txt')
os.remove(sys.argv[6]+'.txt')
os.remove(sys.argv[7]+'.txt')
os.remove(sys.argv[8]+'.txt')
