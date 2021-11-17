import subprocess
import shutil, os
import sys

# generate otpkeys with random data

symfile = ("python sp800_22_tofile.py 833.txt" )
print(symfile)
os.system(symfile)