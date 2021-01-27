#conda install -c conda-forge opencv
import sys
import os
import secrets
import cv2
import hashlib,time
import binascii

i = 0
# generate otpkeys with random data
number = 30
for i in range(number):
    file = str(i) + ".txt"

    output_file = open(file,"wb")

    file_hash = hashlib.sha3_256() # Create the hash object, can use something other than `.sha256()` if you wish
    cap = cv2.VideoCapture(0) # use 0 if you only have front facing camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2250)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

    for x in range(36000):
        ret, frame = cap.read() #read one frame
        #print(frame.shape)
        #file_hash.update(frame) # Update the hash
        #cap.release() # release the VideoCapture object.  
        file_hash.update(frame) # Update the hash
        #print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
        #print (x) # Get the hexadecimal digest of the hash
        output_file.write((file_hash.digest()))



    else:

        output_file.close()



