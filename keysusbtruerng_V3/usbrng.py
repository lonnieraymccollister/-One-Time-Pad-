import subprocess
import shutil, os
import sys

i = 0
# generate otpkeys with random data
number = int(sys.argv[2])-int(sys.argv[1])
for i in range(number):
    file = str(i+int(sys.argv[1])) + ".txt"
    symfile = ("python usbrng1.py " + str(file))
    print(symfile)
    os.system(symfile)