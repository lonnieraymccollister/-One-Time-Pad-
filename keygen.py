#######################
# Python XOR 2 Files
# xor.py
# Jul 2016
# Website: http://www.Megabeets.net
# Use: ./xor.py file1 file2 outputFile
# Example: ./xor.py C:\a.txt C:\b.txt C:\result.txt
#######################

import sys
import os

i = 0

# generate otpkeys with random data
number = 30
for i in range(number):
    file = str(i) + ".txt"
    newfile = open( file , "wb")
    newfile.write (os.urandom(1300000))    # generate x 1 byte random content file
    newfile.close ()
