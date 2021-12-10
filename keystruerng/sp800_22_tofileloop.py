import timeit
import subprocess
import shutil, os
import sys

def loop(i1):
    file = str(i1) + ".txt"
    print(file)
    symfile = ("python sp800_22_tofile.py " + file)
    print(symfile)
    os.system(symfile)


i=0
# generate otpkeys with random data
number = (int(sys.argv[2])+1)-int(sys.argv[1])
for i in range(number):
    i1=i+int(sys.argv[1])
    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    loop(i1)
    print("The time difference is :", timeit.default_timer() - starttime)