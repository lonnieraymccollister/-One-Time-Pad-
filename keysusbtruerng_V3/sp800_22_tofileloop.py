import subprocess
import shutil, os
import sys

i = 0
# generate otpkeys with random data
number = 1000-int(sys.argv[1])
for i in range(number):
    i1=i+int(sys.argv[1])
    file = str(i1) + ".txt"
    print(file)
    symfile = ("python sp800_22_tofile.py " + file)
    print(symfile)
    os.system(symfile)