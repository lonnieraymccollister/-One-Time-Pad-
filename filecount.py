import fnmatch
import sys
import shutil, os

dir_path = r'G:\lonnielaptop\PythonEnvs\One-Time-Pad-main\truerng_v3_000050\keysusbtruerng_V3_0'
count = len(fnmatch.filter(os.listdir(dir_path), '*.txt'))
print('File Count:', count)