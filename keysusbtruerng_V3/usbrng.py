import subprocess
import shutil, os
import sys

i = 0
# generate otpkeys with random data
number = 1000
for i in range(number):
    file = str(i) + ".txt"
    symfile = ("python usbrng1.py " + str(file))
    print(symfile)
    os.system(symfile)