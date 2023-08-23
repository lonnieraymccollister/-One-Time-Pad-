One Time Pad
============
Example
#### Python
#### cd /d E:\(Your path)\keys 
#### Generates 1300 keys
#### python keygen.py
#### cd /d E:\lonnielaptop\PythonEnvs\otp
#### enc.py a.txt 0.txt 0a.txt
#### dec.py 0a.txt 0.txt a.txt
#### One Time pad keys >= message and therefore not breakable.   Vernam -- U.S. Patent 1,310,719, issued July 22, 1919.  The term xor was not used in the patent.  In modern terminology, a Vernam cipher is a symmetrical stream cipher in which the plaintext is combined with a random or pseudorandom stream of data (the "keystream") of the same length, to generate the ciphertext, using the Boolean "exclusive or" (XOR) function.  A famous example of this is the US-Moscow hotline.(point to point).  A sufficient supply of keys have to be prepaired and distributed well in advance of a potential communication which will happen as normal.  
#### OTP Keys must be securely delivered, random, and ===>not reused.<===   There will be a definite cost to setup and maintain.  
#### In the windows 10/11 system all PRNGs in the system are SP800-90 AES_CTR_DRBG with 256-bit security strength using the df() function for seeding and re-seeding(see SP 800-90 for details). Random number generation is very fast.
#### keysusbtruerng_V3 using TrueRNG V3 - USB Hardware Random Number Generator are not guessable.  with 10,400,000-bit security strength.  Random number generation is slow. Key generation using a video camera is slower. Keys can be generated(keygen, videoTrng125k.py, usbrng.py) and tested with autodeletion(sp800_22_tofileloop.py-There is a specification for random numbers and a good RNG can fail up to 25%-35% of time. The python program runs 20x (when converted to cython 6x) slower than the USB RNG) in the directories keyscsprng, keystruerng, and keysusbtruerng_V3 for files that fail to pass the test.
#### However -
#### An OTP can be used to force multifactor authentication - see other repositories
#### An OTP is Quantum secure.
#### An OTP is not experimental and has had a long history of use worldwide.
#### A gui is included -- otp.py -- the key is automatically moved from the keys directory to a used directory.  Keys generated in other directories should be moved to the keys directory and any used keys should be deleted at that time.
#### I recommend registered mail with a return reciept using a micro-sd for secure delivery of keys in order to minimize costs and maximize security. -- See NIST Special Publication 800-53 (Rev. 4) Security and Privacy Controls for Federal Information Systems and Organizations -- SC-37 OUT-OF-BAND CHANNELS -- cryptographic key management information.  Another option is "in person".
####  In the key directory use Combine8OtpFiles.py to increase the size of the Key file.  The keys used will be automatically deleted as reused keys are an attack on the one time pad.  An example of this is ===>> python Combine8OtpFiles.py 1 2 3 4 5 6 7 8 <<===.  The program will automatically add the .txt suffix of the key file. A windows program for the cmd prompt is included ===>> Combine8OtpFiles.exe 1 2 3 4 5 6 7 8 <<===.
#### BinaryToImage.py converts the key file into an image file.  
#### pyinstaller --onefile -w otp.py will create a windows program.(included)
#### (python keygen.py) or in windows (keygen.exe) in the directory keyscsprng will generate 1.3k keys.  Go to that directory(command prompt) and type keygen.exe the command prompt.(included)
#### Checking to see if the key is random is is done with a python program for groups(sp800_22_tofileloop.py) of say 1,000, individually(python sp800_22_tofilename.py(cythonize((recomended)/win11/i7/9min)
#### (python sp800_22_tofileloop.py 0 1000) or (python sp800_22_tofileloop.py Begin# end#) enables checking large numbers of keys)
#### using the windows program (sp800_22_tofileloop.exe 0 1000) or (sp800_22_tofileloop.exe Begin# end#) enables checking large numbers of keys)



