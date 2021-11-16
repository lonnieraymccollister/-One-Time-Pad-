import subprocess
import shutil, os
import sys
from sys import argv,exit

i = 0
# generate otpkeys with random data
number = 1000
for i in range(number):
    i1=i
    file = str(i1+0) + ".txt"
    print(file)
    symfile = ("python sp800_22_tofile.py " + file)
    print(symfile)
    os.system(symfile)