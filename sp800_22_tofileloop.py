import subprocess
import shutil, os
import sys
import time 
import argparse

# Your code here !


i = 0
# generate otpkeys with random data
number = int(sys.argv[2])-int(sys.argv[1])
for i in range(number):
    startTime = time.time()
    i1=i+int(sys.argv[1])
    file = str(i1) + ".txt"
    print(file)
    symfile = ("python sp800_22_tofile.py " + file)
    print(symfile)
    os.system(symfile)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    if executionTime < 9801 :
        f2 = open('sp800_22_TestReport.txt', 'a')
        f2.write(" "  + "\n")
        os.remove(file)
        f2.write(file + " " + str(executionTime) + " " + "Execution time error File Deleted" + "\n")
        f2.close()