One Time Pad
============
Example
#### Python
####cd /d E:\(Your path)\keys
#### Generates 30 or more keys
####python keygen.py
####cd /d E:\lonnielaptop\PythonEnvs\otp
####enc.py a.txt 0.txt 0a.txt
####dec.py 0a.txt 0.txt a.txt
####One Time pad keys >= message and therefore not breakable.   Vernam -- U.S. Patent 1,310,719, issued July 22, 1919.  The term xor was not used in the patent.  In modern terminology, a Vernam cipher is a symmetrical stream cipher in which the plaintext is combined with a random or pseudorandom stream of data (the "keystream") of the same length, to generate the ciphertext, using the Boolean "exclusive or" (XOR) function.  A famous example of this is the US-Moscow hotline. 
####spoiler alert an OTP Keys must be securely delivered and ===>not reused.<===
####However -
####An OTP can be used to force multifactor authentication - see other repositories
####An OTP is Quantum secure.
####An OTP is not experimental and has had a long history of use worldwide.
####A gui is included -- otp.py -- the key is automatically moved from the keys directory to a used directory.
####I recommend registed mail with a return reciept using a micro-sd for secure delivery of keys. -- See NIST Special Publication 800-53 (Rev. 4) Security and Privacy Controls for Federal Information Systems and Organizations -- SC-37 OUT-OF-BAND CHANNELS -- cryptographic key management information.   
####Keys can be generated(keygen, videoTrng125k.py, usbrng.py) and tested(sp800_22_tofileloop.py) in the directories keyscsprng, keystruerng, and keysusbtruerng_V3.






`
